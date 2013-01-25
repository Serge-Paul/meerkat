from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_feedback(request):
   feedback_list = Feedback.objects.all().order_by('-id')
   return render_to_response('feedback/view_all_feedback.html', {'feedback_list': feedback_list})

def create_feedback(request):
   return HttpResponse("You're adding new feedback")

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

