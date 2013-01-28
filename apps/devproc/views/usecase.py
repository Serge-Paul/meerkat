from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class UseCaseForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   target_market = forms.CharField(max_length=200, required=False)
   identifier = forms.CharField(max_length=200)
   source = forms.ChoiceField(choices=SOURCE_CHOICES)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)

def view_all_usecases(request):
   usecase_list = UseCase.objects.all().order_by('-id')
   return render_to_response('usecases/view_all_usecases.html', {'usecase_list': usecase_list})


def create_usecase(request):
   return HttpResponse("You're adding new usecase")

def view_usecase(request, usecase_id):
   usecase = UseCase.objects.get(id = usecase_id)
   return render_to_response('usecases/view_usecase.html', {'usecase': usecase})


def edit_usecase(request, usecase_id):
   return HttpResponse("You're editing usecase %s." % usecase_id)

def delete_usecase(request, usecase_id):

   usecase = UseCase.objects.get(id = usecase_id)
   usecase.delete()

   return redirect('apps.devproc.views.usecase.view_all_usecases')   


