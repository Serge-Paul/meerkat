from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class MilestoneForm(forms.Form):
   title = forms.CharField(max_length=200, error_messages={'required' : 'Please enter a title.'})
   description = forms.CharField(max_length=200, widget=forms.Textarea)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) # ManyToMany
   start_date = forms.DateField()
   end_date = forms.DateField()
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=True) # Foreign Key
   predecessors = forms.ModelMultipleChoiceField(queryset=Milestone.objects.all(), required=False) # ManyToMany
   percent_complete = forms.IntegerField()
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)


def view_all_milestones(request):
   milestone_list = Milestone.objects.all().order_by('-id')
   return render_to_response('milestones/view_all_milestones.html', {'milestone_list': milestone_list})


def create_milestone(request):
   if request.method == 'POST':

      form = MilestoneForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         milestone = Milestone()
         milestone.title = form.cleaned_data['title']
         milestone.description = form.cleaned_data['description']
         milestone.start_date  = form.cleaned_data['start_date']
         milestone.end_date  = form.cleaned_data['end_date']
         milestone.percent_complete = form.cleaned_data['percent_complete']
         milestone.notes  = form.cleaned_data['notes']
         milestone.release  = form.cleaned_data['release']  # Foreign Key
 
         # Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         milestone.save()         

         milestone.category = form.cleaned_data['category'].all() # ManyToMany
	 milestone.predecessors  = form.cleaned_data['predecessors'].all() # ManyToMany

	 milestone.save()

         return redirect('apps.devproc.views.milestone.view_milestone', milestone_id = milestone.id)

      else: #if form is not valid
         return render_to_response('milestones/create_milestone.html', {'form':form, 'message': 'Error creating milestone. Please try again.'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = MilestoneForm()
      return render_to_response('milestones/create_milestone.html', {'form': form},  context_instance=RequestContext(request))


def view_milestone(request, milestone_id):
   milestone = Milestone.objects.get(id = milestone_id)
   return render_to_response('milestones/view_milestone.html', {'milestone': milestone})


def edit_milestone(request, milestone_id):
   return HttpResponse("You're editing milestone %s." % milestone_id)


def delete_milestone(request, milestone_id):

   milestone = Milestone.objects.get(id = milestone_id)
   milestone.delete()

   return redirect('apps.devproc.views.milestone.view_all_milestones')   
                                                              
