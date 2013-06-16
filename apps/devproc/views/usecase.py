from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


class UseCaseForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028, widget=forms.Textarea)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   target_market = forms.CharField(max_length=200, required=False)
   identifier = forms.CharField(max_length=200)
   source = forms.ChoiceField(choices=SOURCE_CHOICES)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)


@login_required
def view_all_usecases(request):
   session_info = get_session_info(request)

   usecase_list = UseCase.objects.all().order_by('-id')
   return render_to_response('usecases/view_all_usecases.html', {'session_info': session_info, 'user' : request.user, 'usecase_list': usecase_list})


@login_required
def create_usecase(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = UseCaseForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         usecase = UseCase()
         usecase.title = form.cleaned_data['title']
         usecase.description = form.cleaned_data['description']
	 usecase.target_market = form.cleaned_data['target_market']
	 usecase.identifier = form.cleaned_data['identifier']
	 usecase.source = form.cleaned_data['source']
	 usecase.notes = form.cleaned_data['notes']
         usecase.product = Product.objects.get(id = session_info['active_product'])

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         usecase.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            usecase.category = form.cleaned_data['category'].all() # ManyToMany
        
         usecase.save()

         return redirect('apps.devproc.views.usecase.view_usecase', usecase_id = usecase.id)

      else: #if form is not valid
         return render_to_response('usecases/create_usecase.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating use case. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = UseCaseForm()
      return render_to_response('usecases/create_usecase.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_usecase(request, usecase_id):
   session_info = get_session_info(request)

   usecase = UseCase.objects.get(id = usecase_id)
   return render_to_response('usecases/view_usecase.html', {'session_info': session_info, 'user' : request.user, 'usecase': usecase})


@login_required
def edit_usecase(request, usecase_id):
   session_info = get_session_info(request)

   usecase = UseCase.objects.get(id = usecase_id)

   if request.method == 'POST':

      form = UseCaseForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         usecase.title = form.cleaned_data['title']
         usecase.description = form.cleaned_data['description']
         usecase.target_market = form.cleaned_data['target_market']
         usecase.identifier = form.cleaned_data['identifier']
         usecase.source = form.cleaned_data['source']
         usecase.notes = form.cleaned_data['notes']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         usecase.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            usecase.category = form.cleaned_data['category'].all() # ManyToMany

         usecase.save()

         return redirect('apps.devproc.views.usecase.view_usecase', usecase_id = usecase.id)

      else: #if form is not valid
         return render_to_response('usecases/create_usecase.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing use case. Please try again.', 'usecase': usecase, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
     
      defaults = {
                 'title' : usecase.title,
                 'description' : usecase.description,
                 'target_market' : usecase.target_market,
                 'identifier' : usecase.identifier,
                 'source' : usecase.source,
                 'notes' : usecase.notes,
                 'category' : usecase.category.all(),
                 }

      form = UseCaseForm(initial=defaults)

      return render_to_response('usecases/create_usecase.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'usecase': usecase, 'mode': 'edit'},  context_instance=RequestContext(request))



@login_required
def delete_usecase(request, usecase_id):
   session_info = get_session_info(request)

   usecase = UseCase.objects.get(id = usecase_id)
   usecase.delete()

   return redirect('apps.devproc.views.usecase.view_all_usecases')   


