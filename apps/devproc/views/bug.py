from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class BugForm(forms.Form):
   title = forms.CharField(max_length=200, label="Bug Title")
   description = forms.CharField(max_length=1028, widget=forms.Textarea)  
   features = forms.ModelMultipleChoiceField(queryset=Feature.objects.all(), required=False) 
   severity = forms.ChoiceField(choices=PRIORITY_CHOICES)
   status = forms.ChoiceField(choices=BUG_STATUS_CHOICES)
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=False) 
   identifier = forms.CharField(max_length=200)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   resolution = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)  


def view_all_bugs(request):
   bug_list = Bug.objects.all().order_by('-id')
   return render_to_response('bugs/view_all_bugs.html', {'bug_list': bug_list})


def create_bug(request, test_id, type):
   if type == 'test':
      test = Test.objects.get(id = test_id)
   
   if type == 'betatest':
      test = BetaTest.objects.get(id = test_id)
   #Need to add error handler here 

   if request.method == 'POST':

      form = BugForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         bug = Bug()
         bug.title = form.cleaned_data['title']
         bug.description  = form.cleaned_data['description']          
         bug.severity = form.cleaned_data['severity']
         bug.status = form.cleaned_data['status']
   	 bug.release = form.cleaned_data['release']
         bug.identifier = form.cleaned_data['identifier']
 	 bug.resolution = form.cleaned_data['resolution']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         bug.save()
         
         bug.features = form.cleaned_data['features'].all()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            bug.category = form.cleaned_data['category'].all() # ManyToMany
        
         if type == 'test':
            bug.test = test

         if type == 'betatest':
            bug.betatest = test

         bug.save()

         return redirect('apps.devproc.views.bug.view_bug', bug_id = bug.id)

      else: #if form is not valid
         return render_to_response('bugs/create_bug.html', {'form':form, 'message': 'Error creating bug. Please try again.', 'test': test, 'type': type}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = BugForm()
      return render_to_response('bugs/create_bug.html', {'form': form, 'test': test, 'type': type},  context_instance=RequestContext(request))


def view_bug(request, bug_id):
   bug = Bug.objects.get(id = bug_id)
   risks = Risk.objects.filter(bug = bug)

   return render_to_response('bugs/view_bug.html', {'bug': bug, 'risks': risks})


def edit_bug(request, bug_id):
   return HttpResponse("You're editing bug %s." % bug_id)

def delete_bug(request, bug_id):

   bug = Bug.objects.get(id = bug_id)
   bug.delete()

   return redirect('apps.devproc.views.bug.view_all_bugs')   
                                                         
