from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


class ComponentForm(forms.Form):
   title = forms.CharField(max_length=200)
   design_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   implementation_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   responsible_engineer= forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False) 
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   parent = forms.ModelChoiceField(queryset=Component.objects.all(), required=False) 
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=False) 
   approval_status = forms.ChoiceField(choices=APPROVAL_STATUS_CHOICES)
   identifier = forms.CharField(max_length=200)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)
   requirements = forms.ModelMultipleChoiceField(queryset=Requirement.objects.all(), required=False)
   usecases = forms.ModelMultipleChoiceField(queryset=UseCase.objects.all(), required=False)

@login_required
def view_all_components(request):
   session_info = get_session_info(request)

   component_list = Component.objects.filter(product = session_info['active_product']).order_by('-id')

   return render_to_response('components/view_all_components.html', {'session_info': session_info, 'user' : request.user, 'component_list': component_list})

@login_required
def create_component(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = ComponentForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         component = Component()
         component.title = form.cleaned_data['title']
 	 component.design_description = form.cleaned_data['design_description']
	 component.implementation_description = form.cleaned_data['implementation_description']
	 component.parent = form.cleaned_data['parent']
	 component.release = form.cleaned_data['release']
	 component.approval_status = form.cleaned_data['approval_status']
	 component.identifier = form.cleaned_data['identifier']
	 component.notes = form.cleaned_data['notes']
         component.product = session_info['active_product']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         component.save()

         if form.cleaned_data['responsible_engineer']:
	    component.responsible_engineer = form.cleaned_data['responsible_engineer'].all()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            component.category = form.cleaned_data['category'].all() # ManyToMany
         
         if form.cleaned_data['requirements']:
	    component.requirements = form.cleaned_data['requirements'].all()
	
         if form.cleaned_data['usecases']: 
            component.usecases = form.cleaned_data['usecases'].all()

         component.save()

         return redirect('apps.devproc.views.component.view_component', component_id = component.id)

      else: #if form is not valid
         return render_to_response('components/create_component.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating component. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = ComponentForm()
      return render_to_response('components/create_component.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))

@login_required
def view_component(request, component_id):
   session_info = get_session_info(request)

   component = Component.objects.get(id = component_id)
   risks = Risk.objects.filter(component = component)
   attributes = Attribute.objects.filter(component = component)   

   return render_to_response('components/view_component.html', {'session_info': session_info, 'user' : request.user, 'component': component, 'risks': risks, 'attributes': attributes})


@login_required
def edit_component(request, component_id):
   session_info = get_session_info(request)
   
   component = Component.objects.get(id = component_id)

   if request.method == 'POST':

      form = ComponentForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         component.title = form.cleaned_data['title']
         component.design_description = form.cleaned_data['design_description']
         component.implementation_description = form.cleaned_data['implementation_description']
         component.parent = form.cleaned_data['parent']
         component.release = form.cleaned_data['release']
         component.approval_status = form.cleaned_data['approval_status']
         component.identifier = form.cleaned_data['identifier']
         component.notes = form.cleaned_data['notes']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         component.save()

         if form.cleaned_data['responsible_engineer']:
            component.responsible_engineer = form.cleaned_data['responsible_engineer'].all()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            component.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['requirements']:
            component.requirements = form.cleaned_data['requirements'].all()

         if form.cleaned_data['usecases']:
            component.usecases = form.cleaned_data['usecases'].all()

         component.save()

         return redirect('apps.devproc.views.component.view_component', component_id = component.id)

      else: #if form is not valid
         return render_to_response('components/create_component.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing component. Please try again.', 'component': component, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      
      defaults = {
                 'title' : component.title,
                 'design_description': component.design_description,
                 'implementation_description': component.implementation_description,
		 'parent' : component.parent,
                 'release' : component.release,
                 'approval_status' : component.approval_status,
                 'identifier' : component.identifier,
                 'notes' : component.notes,
                 'responsible_engineer' : component.responsible_engineer.all(),
                 'category' : component.category.all(),
                 'requirements' : component.requirements.all(),
                 'usecases' : component.usecases.all(),
                 }

      form = ComponentForm(initial=defaults)

      return render_to_response('components/create_component.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'component': component, 'mode': 'edit'},  context_instance=RequestContext(request))


@login_required
def delete_component(request, component_id):
   session_info = get_session_info(request)

   component = Component.objects.get(id = component_id)
   component.delete()

   return redirect('apps.devproc.views.component.view_all_components')   
                                                             
