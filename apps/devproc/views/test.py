from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


class TestForm(forms.Form):
   title = forms.CharField(max_length=200)
   test_description = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)
   implementation_description = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
   features = forms.ModelMultipleChoiceField(queryset=Feature.objects.all(), required=False, label="Supporting Features")
   responsible_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False, label="Test Engineer") 
   pass_fail_criteria = forms.CharField(max_length=1028, required=False)
   status = forms.ChoiceField(choices=TEST_STATUS_CHOICES)
   identifier = forms.CharField(max_length=200)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)  

@login_required
def view_all_tests(request):
   session_info = get_session_info(request)

   test_list = Test.objects.filter(product = session_info['active_product']).order_by('-id')

   return render_to_response('tests/view_all_tests.html', {'session_info': session_info, 'user' : request.user, 'test_list': test_list})


@login_required
def create_test(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = TestForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         test = Test()
         test.title = form.cleaned_data['title']
         test.test_description = form.cleaned_data['test_description']
	 test.implementation_description = form.cleaned_data['implementation_description']
	 test.pass_fail_criteria = form.cleaned_data['pass_fail_criteria']
	 test.status = form.cleaned_data['status']
	 test.identifier = form.cleaned_data['identifier']
         test.product = session_info['active_product']
         test.notes = form.cleaned_data['notes']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         test.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            test.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['features']:
	    test.features = form.cleaned_data['features'].all()        

         if form.cleaned_data['responsible_engineer']:
	    test.responsible_engineer = form.cleaned_data['responsible_engineer'].all()

         test.save()

         return redirect('apps.devproc.views.test.view_test', test_id = test.id)

      else: #if form is not valid
         return render_to_response('tests/create_test.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating test. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = TestForm()
      return render_to_response('tests/create_test.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_test(request, test_id):
   session_info = get_session_info(request)

   test = Test.objects.get(id = test_id)
   bugs = Bug.objects.filter(test = test_id)
   return render_to_response('tests/view_test.html', {'session_info': session_info, 'user' : request.user, 'test': test, 'bugs': bugs})


@login_required
def edit_test(request, test_id):
   session_info = get_session_info(request)

   test = Test.objects.get(id = test_id)

   if request.method == 'POST':

      form = TestForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         test.title = form.cleaned_data['title']
         test.test_description = form.cleaned_data['test_description']
         test.implementation_description = form.cleaned_data['implementation_description']
         test.pass_fail_criteria = form.cleaned_data['pass_fail_criteria']
         test.status = form.cleaned_data['status']
         test.identifier = form.cleaned_data['identifier']
         test.notes = form.cleaned_data['notes']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         test.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            test.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['features']:
            test.features = form.cleaned_data['features'].all()

         if form.cleaned_data['responsible_engineer']:
            test.responsible_engineer = form.cleaned_data['responsible_engineer'].all()

         test.save()

         return redirect('apps.devproc.views.test.view_test', test_id = test.id)

      else: #if form is not valid
         return render_to_response('tests/create_test.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing test. Please try again.', 'test': test, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form

      defaults = {
                 'title' : test.title,
                 'test_description' : test.test_description,
                 'implementation_description' : test.implementation_description,
                 'pass_fail_criteria' : test.pass_fail_criteria,
                 'status' : test.status,
                 'identifier': test.identifier,
                 'category' : test.category.all(),
                 'features' : test.features.all(),
                 'responsible_engineer' : test.responsible_engineer.all(),
                 'notes': test.notes,
                 }

      form = TestForm(initial=defaults)


      return render_to_response('tests/create_test.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'test': test, 'mode': 'edit'},  context_instance=RequestContext(request))




@login_required
def delete_test(request, test_id):
   session_info = get_session_info(request)

   test = Test.objects.get(id = test_id)
   test.delete()

   return redirect('apps.devproc.views.test.view_all_tests')   

