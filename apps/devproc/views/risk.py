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

def create_risk(request, obj_id, type):

   if type == "component":
      obj = Component.objects.get(id = obj_id)

   if type == "feature":
      obj = Feature.objects.get(id = obj_id)

   if type == "bug":
      obj = Bug.objects.get(id = obj_id)


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

         if type == "component":
            risk.component = obj

         if type == "feature":
            risk.feature = obj

         if type == "bug":
            risk.bug = obj

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            risk.category = form.cleaned_data['category'].all() # ManyToMany
        
         risk.save()

         return redirect('apps.devproc.views.risk.view_risk', risk_id = risk.id)

      else: #if form is not valid
         return render_to_response('risks/create_risk.html', {'form':form, 'message': 'Error creating risk. Please try again.', 'obj': obj, 'type': type, 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = RiskForm()
      return render_to_response('risks/create_risk.html', {'form': form, 'obj': obj, 'type': type, 'mode': 'create'},  context_instance=RequestContext(request))


def view_risk(request, risk_id):
   risk = Risk.objects.get(id = risk_id)
   
   feature = None
   component = None
   bug = None

   if risk.feature:
	feature = Feature.objects.get(id = risk.feature.id)

   if risk.component:
        component = Component.objects.get(id = risk.component.id)

   if risk.bug:
        bug = Bug.objects.get(id = risk.bug.id)

   return render_to_response('risks/view_risk.html', {'risk': risk, 'feature': feature, 'component': component, 'bug': bug})

def edit_risk(request, risk_id):

   risk = Risk.objects.get(id = risk_id)

   if risk.component:
      type = "component"
      obj = risk.component

   if risk.feature:
      type = "feature"
      obj = risk.feature

   if risk.bug:
      type = "bug"
      obj = risk.bug

   if request.method == 'POST':

      form = RiskForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

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
         return render_to_response('risks/create_risk.html', {'form':form, 'message': 'Error editing risk. Please try again.', 'obj': obj, 'type': type, 'risk': risk, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form

      defaults = {
                 'title' : risk.title,
                 'description' : risk.description,
                 'release' : risk.release,
                 'probability' : risk.probability,
                 'severity' : risk.severity,
                 'status' : risk.status,
                 'identifier' : risk.identifier,
                 'approval_status' : risk.approval_status,
                 'category' : risk.category.all(),
                 }

      form = RiskForm(initial=defaults)

      return render_to_response('risks/create_risk.html', {'form': form, 'obj': obj, 'type': type, 'risk': risk, 'mode': 'edit'},  context_instance=RequestContext(request))


def delete_risk(request, risk_id):

   risk = Risk.objects.get(id = risk_id)
   risk.delete()

   return redirect('apps.devproc.views.risk.view_all_risks')   

