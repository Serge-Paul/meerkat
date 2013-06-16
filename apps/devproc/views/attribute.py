from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *

class AttributeForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028)
  
@login_required
def view_all_attributes(request, component_id):

#View all attributes associated with a specific component

   component = Component.objects.get(id = component_id)
   attribute_list = Attribute.objects.filter(component = component)

   session_info = get_session_info(request)

   return render_to_response('attributes/view_all_attributes.html', {'session_info': session_info, 'user' : request.user, 'attribute_list': attribute_list, 'component': component})
 
@login_required
def create_attribute(request, component_id):
   
   session_info = get_session_info(request)

   component = Component.objects.get(id = component_id)

   if request.method == 'POST':

      form = AttributeForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         attribute = Attribute()
         attribute.title = form.cleaned_data['title']
         attribute.description = form.cleaned_data['description']            

         attribute.component = component
 
         attribute.save()
      
         return redirect('apps.devproc.views.attribute.view_attribute', component_id = component.id, attribute_id = attribute.id)

      else: #if form is not valid
         return render_to_response('attributes/create_attribute.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating attribute. Please try again.', 'component': component, 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = AttributeForm()
      return render_to_response('attributes/create_attribute.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'component': component, 'mode': 'create'},  context_instance=RequestContext(request))

@login_required
def view_attribute(request, component_id, attribute_id):
   session_info = get_session_info(request)

   attribute = Attribute.objects.get(id = attribute_id)
   component = Component.objects.get(id = component_id)
   return render_to_response('attributes/view_attribute.html', {'session_info': session_info, 'user' : request.user, 'attribute': attribute, 'component': component})

@login_required
def edit_attribute(request, attribute_id):
   session_info = get_session_info(request)

   attribute = Attribute.objects.get(id = attribute_id)

   if request.method == 'POST':

      form = AttributeForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         attribute.title = form.cleaned_data['title']
         attribute.description = form.cleaned_data['description']

         attribute.save()

         return redirect('apps.devproc.views.attribute.view_attribute', component_id = attribute.component.id, attribute_id = attribute.id)

      else: #if form is not valid
         return render_to_response('attributes/create_attribute.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing attribute. Please try again.', 'component': attribute.component, 'attribute': attribute, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      
      defaults = {
                 'title' : attribute.title,
                 'description': attribute.description,
                 }

      form = AttributeForm(initial=defaults)

      return render_to_response('attributes/create_attribute.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'component': attribute.component, 'attribute': attribute, 'mode': 'edit'},  context_instance=RequestContext(request))


@login_required
def delete_attribute(request, attribute_id):
   session_info = get_session_info(request)

   attribute = Attribute.objects.get(id = attribute_id)
   
   component = attribute.component 

   attribute.delete()

   return redirect('apps.devproc.views.attribute.view_all_attributes', component_id = component.id)   



