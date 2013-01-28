from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class BugForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028, widget=forms.Textarea)  
   features = forms.ModelMultipleChoiceField(queryset=Feature.objects.all(), required=False) 
   severity = forms.ChoiceField(choices=PRIORITY_CHOICES)
   status = forms.ChoiceField(choices=BUG_STATUS_CHOICES)
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=False) 
   test = forms.ModelChoiceField(queryset=Test.objects.all(), required=False) 
   identifier = forms.CharField(max_length=200)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   resolution = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)  
   betatest = forms.ModelChoiceField(queryset=BetaTest.objects.all(), required=False) 
   risk = forms.ModelChoiceField(queryset=Risk.objects.all(), required=False) 


def view_all_bugs(request):
   bug_list = Bug.objects.all().order_by('-id')
   return render_to_response('bugs/view_all_bugs.html', {'bug_list': bug_list})


def create_bug(request):
   return HttpResponse("You're adding new bug")

def view_bug(request, bug_id):
   bug = Bug.objects.get(id = bug_id)
   return render_to_response('bugs/view_bug.html', {'bug': bug})


def edit_bug(request, bug_id):
   return HttpResponse("You're editing bug %s." % bug_id)

def delete_bug(request, bug_id):

   bug = Bug.objects.get(id = bug_id)
   bug.delete()

   return redirect('apps.devproc.views.bug.view_all_bugs')   
                                                         
