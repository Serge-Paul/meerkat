from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


class MilestoneForm(forms.Form):
   title = forms.CharField(max_length=200, error_messages={'required' : 'Please enter a title.'})
   description = forms.CharField(max_length=1028, widget=forms.Textarea)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) # ManyToMany
   start_date = forms.DateField()
   end_date = forms.DateField()
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=True) # Foreign Key
   predecessors = forms.ModelMultipleChoiceField(queryset=Milestone.objects.all(), required=False) # ManyToMany
   percent_complete = forms.IntegerField()
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)


@login_required
def view_all_milestones(request):
   session_info = get_session_info(request)

   milestone_list = Milestone.objects.all().order_by('-id')
   return render_to_response('milestones/view_all_milestones.html', {'session_info': session_info, 'user' : request.user, 'milestone_list': milestone_list})


@login_required
def create_milestone(request):
   session_info = get_session_info(request)

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
         milestone.product = Product.objects.get(id = session_info['active_product']) 

         # Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         milestone.save()         

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            milestone.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['predecessors']:
	    milestone.predecessors  = form.cleaned_data['predecessors'].all() # ManyToMany

	 milestone.save()

         return redirect('apps.devproc.views.milestone.view_milestone', milestone_id = milestone.id)

      else: #if form is not valid
         Milestone.objects.get(id = milestone_id)
         
         return render_to_response('milestones/create_milestone.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating milestone. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = MilestoneForm()
      return render_to_response('milestones/create_milestone.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_milestone(request, milestone_id):
   session_info = get_session_info(request)

   milestone = Milestone.objects.get(id = milestone_id)
   return render_to_response('milestones/view_milestone.html', {'session_info': session_info, 'user' : request.user, 'milestone': milestone})


@login_required
def edit_milestone(request, milestone_id):
   session_info = get_session_info(request)

   milestone = Milestone.objects.get(id = milestone_id)

   if request.method == 'POST':

      form = MilestoneForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         milestone.title = form.cleaned_data['title']
         milestone.description = form.cleaned_data['description']
         milestone.start_date  = form.cleaned_data['start_date']
         milestone.end_date  = form.cleaned_data['end_date']
         milestone.percent_complete = form.cleaned_data['percent_complete']
         milestone.notes  = form.cleaned_data['notes']
         milestone.release  = form.cleaned_data['release']  # Foreign Key

         # Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         milestone.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            milestone.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['predecessors']:
            milestone.predecessors  = form.cleaned_data['predecessors'].all() # ManyToMany

         milestone.save()

         return redirect('apps.devproc.views.milestone.view_milestone', milestone_id = milestone.id)

      else: #if form is not valid
         return render_to_response('milestones/create_milestone.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing milestone. Please try again.', 'milestone': milestone, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
  
      defaults = {
                 'title' : milestone.title,
                 'description' : milestone.description,
                 'start_date' : milestone.start_date,
                 'end_date' : milestone.end_date,
                 'percent_complete' : milestone.percent_complete,
                 'notes' : milestone.notes,
                 'release' : milestone.release,
                 'category' : milestone.category.all(),
                 'predecessors' : milestone.predecessors.all(),               
                 }

      form = MilestoneForm(initial=defaults)

      return render_to_response('milestones/create_milestone.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'milestone': milestone, 'mode': 'edit'},  context_instance=RequestContext(request))



@login_required
def delete_milestone(request, milestone_id):
   session_info = get_session_info(request)

   milestone = Milestone.objects.get(id = milestone_id)
   milestone.delete()

   return redirect('apps.devproc.views.milestone.view_all_milestones')   
                                                              
