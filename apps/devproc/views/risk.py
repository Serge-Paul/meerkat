from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *
from itertools import chain

class RiskForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028, widget=forms.Textarea)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),required=False)
   probability = forms.ChoiceField(choices=PROBABILITY_CHOICES)
   severity = forms.ChoiceField(choices=PRIORITY_CHOICES)
   status = forms.ChoiceField(choices=RISK_CHOICES)
   identifier = forms.CharField(max_length=200)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)

@login_required
def view_all_risks(request):
   session_info = get_session_info(request)

   feature_risk_list = Risk.objects.filter(feature__product = session_info['active_product'].id).order_by('-id')
   component_risk_list = Risk.objects.filter(component__product = session_info['active_product'].id).order_by('-id')
   test_bug_risk_list = Risk.objects.filter(bug__test__product = session_info['active_product'].id).order_by('-id')
   betatest_bug_risk_list = Risk.objects.filter(bug__betatest__release__product = session_info['active_product'].id).order_by('-id')

   risk_list = sorted(
    chain(feature_risk_list, component_risk_list, test_bug_risk_list, betatest_bug_risk_list),
    key=lambda instance: instance.id)


   return render_to_response('risks/view_all_risks.html', {'session_info': session_info, 'user' : request.user, 'risk_list': risk_list})


@login_required
def create_risk(request, obj_id, type):
   session_info = get_session_info(request)

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
         risk.probability = form.cleaned_data['probability']
         risk.severity = form.cleaned_data['severity']
         risk.status = form.cleaned_data['status']
         risk.identifier = form.cleaned_data['identifier']
         risk.notes = form.cleaned_data['notes']

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
         return render_to_response('risks/create_risk.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating risk. Please try again.', 'obj': obj, 'type': type, 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = RiskForm()
      return render_to_response('risks/create_risk.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'obj': obj, 'type': type, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_risk(request, risk_id):
   session_info = get_session_info(request)

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

   return render_to_response('risks/view_risk.html', {'session_info': session_info, 'user' : request.user, 'risk': risk, 'feature': feature, 'component': component, 'bug': bug})


@login_required
def edit_risk(request, risk_id):
   session_info = get_session_info(request)

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
         risk.probability = form.cleaned_data['probability']
         risk.severity = form.cleaned_data['severity']
         risk.status = form.cleaned_data['status']
         risk.identifier = form.cleaned_data['identifier']
         risk.notes = form.cleaned_data['notes']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         risk.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            risk.category = form.cleaned_data['category'].all() # ManyToMany

         risk.save()

         return redirect('apps.devproc.views.risk.view_risk', risk_id = risk.id)

      else: #if form is not valid
         return render_to_response('risks/create_risk.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing risk. Please try again.', 'obj': obj, 'type': type, 'risk': risk, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form

      defaults = {
                 'title' : risk.title,
                 'description' : risk.description,
                 'probability' : risk.probability,
                 'severity' : risk.severity,
                 'status' : risk.status,
                 'identifier' : risk.identifier,
                 'category' : risk.category.all(),
                 'notes' : risk.notes,
                 }

      form = RiskForm(initial=defaults)

      return render_to_response('risks/create_risk.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'obj': obj, 'type': type, 'risk': risk, 'mode': 'edit'},  context_instance=RequestContext(request))


@login_required
def delete_risk(request, risk_id):
   session_info = get_session_info(request)

   risk = Risk.objects.get(id = risk_id)
   risk.delete()

   return redirect('apps.devproc.views.risk.view_all_risks')   

