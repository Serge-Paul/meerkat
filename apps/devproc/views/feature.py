from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class FeatureForm(forms.Form):
   title = forms.CharField(max_length=200)
   design_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   implementation_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   responsible_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False) 
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=True) 
   approval_status = forms.ChoiceField(choices=APPROVAL_STATUS_CHOICES)
   usecases = forms.ModelMultipleChoiceField(queryset=UseCase.objects.all(), required=False) 
   requirements = forms.ModelMultipleChoiceField(queryset=Requirement.objects.all(), required=False) 
   identifier = forms.CharField(max_length=200)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False) 
   component = forms.ModelMultipleChoiceField(queryset=Component.objects.all(), required=False) 
   risk = forms.ModelChoiceField(queryset=Risk.objects.all(), required=False) 


def view_all_features(request):
   feature_list = Feature.objects.all().order_by('-id')
   return render_to_response('features/view_all_features.html', {'feature_list': feature_list})



def create_feature(request):
   return HttpResponse("You're adding new feature")

def view_feature(request, feature_id):
   feature = Feature.objects.get(id = feature_id)
   return render_to_response('features/view_feature.html', {'feature': feature})


def edit_feature(request, feature_id):
   return HttpResponse("You're editing feature %s." % feature_id)


def delete_feature(request, feature_id):

   feature = Feature.objects.get(id = feature_id)
   feature.delete()

   return redirect('apps.devproc.views.feature.view_all_features')   
                                                              
