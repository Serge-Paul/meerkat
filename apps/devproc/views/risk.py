from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class RiskForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=200, widget=forms.Textarea)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),required=False)
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=False)
   probability = forms.ChoiceField(choices=PROBABILITY_CHOICES)
   severity = forms.ChoiceField(choices=PRIORITY_CHOICES)
   status = forms.ChoiceField(choices=RISK_CHOICES)
   identifier = forms.CharField(max_length=200)
   approval_status = forms.ChoiceField(choices=APPROVAL_STATUS_CHOICES)


def view_all_risks(request):
   risk_list = Risk.objects.all().order_by('-id')
   return render_to_response('risks/view_all_risks.html', {'risk_list': risk_list})

def create_risk(request):
   if request.method == 'POST':

      form = RiskForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         risk = Risk()
         risk.title = form.cleaned_data['title']
         risk.description  = form.cleaned_data['description']
         risk.release = form.cleaned_data['release']
         risk.probability = form.cleaned_data['probability']
         risk.severity = form.cleaned_data['severity']
         risk.status = form.cleaned_data['status']
         risk.identifier = form.cleaned_data['identifier']
         risk.approval_status = form.cleaned_data['approval_status']         

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         risk.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            risk.category = form.cleaned_data['category'].all() # ManyToMany
        
         risk.save()

         return redirect('apps.devproc.views.risk.view_risk', risk_id = risk.id)

      else: #if form is not valid
         return render_to_response('risks/create_risk.html', {'form':form, 'message': 'Error creating risk. Please try again.'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = RiskForm()
      return render_to_response('risks/create_risk.html', {'form': form},  context_instance=RequestContext(request))


def view_risk(request, risk_id):
   risk = Risk.objects.get(id = risk_id)
   component = Component.objects.filter(risk = risk_id)
   bug = Bug.objects.filter(risk = risk_id)
   feature = Feature.objects.filter(risk = risk_id)

   return render_to_response('risks/view_risk.html', {'risk': risk, 'bug': bug, 'component': component, 'feature': feature})

def edit_risk(request, risk_id):
   return HttpResponse("You're editing risk %s." % risk_id)

def delete_risk(request, risk_id):

   risk = Risk.objects.get(id = risk_id)
   risk.delete()

   return redirect('apps.devproc.views.risk.view_all_risks')   

