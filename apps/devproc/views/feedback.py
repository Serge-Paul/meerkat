from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class FeedbackForm(forms.Form):
   betatest = forms.ModelChoiceField(queryset=BetaTest.objects.all(), required=True) 
   customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True) 
   feedback = forms.CharField(max_length=1028, widget=forms.Textarea)


def view_all_feedback(request):
   feedback_list = Feedback.objects.all().order_by('-id')
   return render_to_response('feedback/view_all_feedback.html', {'feedback_list': feedback_list})

def create_feedback(request, feature_id):

   feature =  Feature.objects.get(id = feature_id)

   if request.method == 'POST':

      form = FeedbackForm(request.POST)

      # Do when form is submitted
      if form.is_valid():
         #NEED TO change this so that customer field is auto-linked to currently logged in user, and need to delete customer from form above
         feedback = Feedback()
         feedback.betatest = form.cleaned_data['betatest']
         feedback.customer = form.cleaned_data['customer']
 	 feedback.feature = feature
	 feedback.feedback = form.cleaned_data['feedback']

         feedback.save()

         return redirect('apps.devproc.views.feedback.view_feedback', betatest_id = feedback.betatest.id, customer_id = feedback.customer.id)

      else: #if form is not valid
         return render_to_response('feedback/create_feedback.html', {'form':form, 'message': 'Error saving feedback. Please try again.', 'feature': feature}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = FeedbackForm()
      return render_to_response('feedback/create_feedback.html', {'form': form, 'feature': feature},  context_instance=RequestContext(request))


def view_feedback(request, betatest_id, customer_id):
   #get list of all feedbacks for a certain beta test and specific customer
   feedback_list = Feedback.objects.filter(betatest = betatest_id, customer = customer_id)
 
   return render_to_response('feedback/view_feedback.html', {'feedback_list': feedback_list})

def edit_feedback(request, feedback_id):
   return HttpResponse("You're editing feedback %s." % feedback_id)

def delete_feedback(request, feedback_id):

   feedback = Feedback.objects.get(id = feedback_id)
   feedback.delete()

   return redirect('apps.devproc.views.feedback.view_all_feedback')

