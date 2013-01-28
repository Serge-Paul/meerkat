from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class TestForm(forms.Form):
   title = forms.CharField(max_length=200)
   test_description = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)
   implementation_description = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
   features = forms.ModelMultipleChoiceField(queryset=Feature.objects.all(), required=False)
   responsible_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False) 
   pass_fail_criteria = forms.CharField(max_length=1028, required=False)
   status = forms.ChoiceField(choices=TEST_STATUS_CHOICES)
   identifier = forms.CharField(max_length=200)
  

def view_all_tests(request):
   test_list = Test.objects.all().order_by('-id')
   return render_to_response('tests/view_all_tests.html', {'test_list': test_list})

def create_test(request):
   return HttpResponse("You're adding new test")

def view_test(request, test_id):
   test = Test.objects.get(id = test_id)
   bugs = Bug.objects.filter(test = test_id)
   return render_to_response('tests/view_test.html', {'test': test, 'bugs': bugs})

def edit_test(request, test_id):
   return HttpResponse("You're editing test %s." % test_id)

def delete_test(request, test_id):

   test = Test.objects.get(id = test_id)
   test.delete()

   return redirect('apps.devproc.views.test.view_all_tests')   

