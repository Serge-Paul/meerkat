from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class ComponentForm(forms.Form):
   title = forms.CharField(max_length=200)
   design_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   implementation_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   responsible_engineer= forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False) 
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   attributes= forms.ModelMultipleChoiceField(queryset=Attribute.objects.all(), required=False) 
   parent = forms.ModelChoiceField(queryset=Component.objects.all(), required=False) 
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=False) 
   approval_status = forms.ChoiceField(choices=APPROVAL_STATUS_CHOICES)
   identifier = forms.CharField(max_length=200)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)
   requirements = forms.ModelMultipleChoiceField(queryset=Requirement.objects.all(), required=False)
   usecases = forms.ModelMultipleChoiceField(queryset=UseCase.objects.all(), required=False)
   risk = forms.ModelChoiceField(queryset=Risk.objects.all(), required=False)


def view_all_components(request):
   component_list = Component.objects.all().order_by('-id')
   return render_to_response('components/view_all_components.html', {'component_list': component_list})


def create_component(request):
   return HttpResponse("You're adding new component")

def view_component(request, component_id):
  component = Component.objects.get(id = component_id)
  return render_to_response('components/view_component.html', {'component': component})


def edit_component(request, component_id):
   return HttpResponse("You're editing component %s." % component_id)


def delete_component(request, component_id):

   component = Component.objects.get(id = component_id)
   component.delete()

   return redirect('apps.devproc.views.component.view_all_components')   
                                                             
