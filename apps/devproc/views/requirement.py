from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class RequirementForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   parent = forms.ModelChoiceField(queryset=Requirement.objects.all(), required=False) #need to prevent chosing current reqmt as parent
   use_case = forms.ModelChoiceField(queryset=UseCase.objects.all(), required=False)
   priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=False)
   approval_status = forms.ChoiceField(choices=APPROVAL_STATUS_CHOICES)
   identifier = forms.CharField(max_length=200)
   source = forms.ChoiceField(choices=SOURCE_CHOICES)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)  



def view_all_reqmts(request): 
   reqmt_list = Requirement.objects.all().order_by('-id') 
   return render_to_response('requirements/view_all_reqmts.html', {'reqmt_list': reqmt_list})

def create_reqmt(request):
   return HttpResponse("You're adding new reqmt")

def view_reqmt(request, reqmt_id):
   reqmt = Requirement.objects.get(id = reqmt_id)
   return render_to_response('requirements/view_reqmt.html', {'reqmt': reqmt})

def edit_reqmt(request, reqmt_id):
   return HttpResponse("You're editing reqmt %s." % reqmt_id)


def delete_reqmt(request, reqmt_id):

   reqmt = Requirement.objects.get(id = reqmt_id)
   reqmt.delete()

   return redirect('apps.devproc.views.requirements.view_all_reqmts')   

