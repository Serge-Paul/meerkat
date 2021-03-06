from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *

class BetaTestForm(forms.Form):
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=True) 
   responsible_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False) 

@login_required
def view_all_betatests(request):
   session_info = get_session_info(request)

   #betatest_list = BetaTest.objects.all().order_by('-id')
   betatest_list = BetaTest.objects.filter(release__product = session_info['active_product']).order_by('-id')

   return render_to_response('betatests/view_all_betatests.html', {'session_info': session_info, 'user' : request.user, 'betatest_list': betatest_list})

@login_required
def create_betatest(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = BetaTestForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         betatest = BetaTest()
         betatest.release = form.cleaned_data['release']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         betatest.save()

         betatest.responsible_engineer = form.cleaned_data['responsible_engineer'].all() # ManyToMany
        
         betatest.save()

         return redirect('apps.devproc.views.betatest.view_betatest', betatest_id = betatest.id)

      else: #if form is not valid
         return render_to_response('betatests/create_betatest.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating beta test. Please try again.'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = BetaTestForm()
      return render_to_response('betatests/create_betatest.html', {'session_info': session_info, 'user' : request.user, 'form': form},  context_instance=RequestContext(request))

@login_required
def view_betatest(request, betatest_id):
   session_info = get_session_info(request)

   betatest = BetaTest.objects.get(id = betatest_id)
   feedback_list = Feedback.objects.filter(betatest = betatest_id)
   bugs = Bug.objects.filter(betatest = betatest_id)

   return render_to_response('betatests/view_betatest.html', {'session_info': session_info, 'user' : request.user, 'betatest': betatest, 'feedback_list': feedback_list, 'bugs': bugs})



@login_required
def delete_betatest(request, betatest_id):
   session_info = get_session_info(request)

   betatest = BetaTest.objects.get(id = betatest_id)
   betatest.delete()

   return redirect('apps.devproc.views.betatest.view_all_betatests')   


