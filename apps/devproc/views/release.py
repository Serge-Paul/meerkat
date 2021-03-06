from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *
from itertools import chain

class ReleaseForm(forms.Form):
   name = forms.CharField(max_length=200, label="Name")
   release_date = forms.DateField()
   pass_fail_criteria = forms.CharField(max_length=1028, required=False, label="Pass/fail criteria")
   market = forms.CharField(max_length=200, required=False, label="Target market")
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)  
   release_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False, label="Release Manager") 
   goals = forms.CharField(max_length=1028, required=False, label="Goals/Themes")
   product_manager = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False, label="Product Manager")


@login_required
def view_all_releases(request):
   session_info = get_session_info(request)

   release_list = Release.objects.filter(product = session_info['active_product']).order_by('-id')

   return render_to_response('releases/view_all_releases.html', {'session_info': session_info, 'user' : request.user, 'release_list': release_list})


@login_required
def create_release(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = ReleaseForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         release = Release()
         release.name = form.cleaned_data['name']
         release.release_date = form.cleaned_data['release_date']
	 release.pass_fail_criteria = form.cleaned_data['pass_fail_criteria']
	 release.market = form.cleaned_data['market']
	 release.notes = form.cleaned_data['notes']
	 release.goals = form.cleaned_data['goals']
         release.product = session_info['active_product']
 
# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         release.save()
         
         if form.cleaned_data['release_engineer']:
            release.responsible_engineer = form.cleaned_data['release_engineer'].all() # ManyToMany

         if form.cleaned_data['product_manager']:
            release.product_manager = form.cleaned_data['product_manager'].all() # ManyToMany

         release.save()

         # Automatically create betatest object whenever create new release

         betatest = BetaTest()

         betatest.release = release
         betatest.save()


         return redirect('apps.devproc.views.release.view_release', release_id = release.id)

      else: #if form is not valid
         return render_to_response('releases/create_release.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating release. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = ReleaseForm()
      return render_to_response('releases/create_release.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_release(request, release_id):
   session_info = get_session_info(request)

   release = Release.objects.get(id = release_id)
   features = Feature.objects.filter(release = release_id)

   bug_risks = Risk.objects.filter(bug__release = release_id)
   feature_risks = Risk.objects.filter(feature__release = release_id)
   component_risks = Risk.objects.filter(component__release = release_id)

   risks = sorted(
    chain(bug_risks, feature_risks, component_risks),
    key=lambda instance: instance.id)

   bugs = Bug.objects.filter(release = release_id)
   milestones = Milestone.objects.filter(release = release_id)

   betatest = BetaTest.objects.get(release = release_id)

   return render_to_response('releases/view_release.html', {'session_info': session_info, 'user' : request.user, 'release': release,'features':features , 'risks':risks, 'bugs': bugs, 'milestones': milestones, 'betatest': betatest })


@login_required
def edit_release(request, release_id):
   session_info = get_session_info(request)

   release = Release.objects.get(id = release_id)
   betatest = BetaTest.objects.get(release = release) 

   if request.method == 'POST':

      form = ReleaseForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         release.name = form.cleaned_data['name']
         release.release_date = form.cleaned_data['release_date']
         release.pass_fail_criteria = form.cleaned_data['pass_fail_criteria']
         release.market = form.cleaned_data['market']
         release.notes = form.cleaned_data['notes']
         release.goals = form.cleaned_data['goals']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         release.save()

         if form.cleaned_data['release_engineer']:
            release.responsible_engineer = form.cleaned_data['release_engineer'].all() # ManyToMany

         if form.cleaned_data['product_manager']:
            release.product_manager = form.cleaned_data['product_manager'].all() # ManyToMany

         release.save()


         return redirect('apps.devproc.views.release.view_release', release_id = release.id)

      else: #if form is not valid
         return render_to_response('releases/create_release.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing release. Please try again.', 'release': release, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
     
      defaults = {
                 'name' : release.name,
                 'release_date' : release.release_date,
                 'pass_fail_criteria' : release.pass_fail_criteria,
                 'market' : release.market,
                 'notes' : release.notes,
                 'goals' : release.goals,
                 'release_engineer' : release.responsible_engineer.all(),
                 'product_manager' : release.product_manager.all(),               
                 }

      form = ReleaseForm(initial=defaults)

      return render_to_response('releases/create_release.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'release': release, 'mode': 'edit'},  context_instance=RequestContext(request))


@login_required
def delete_release(request, release_id):
   session_info = get_session_info(request)

   release = Release.objects.get(id = release_id)
   release.delete()

   # automatically delete the beta test associated with this release
   betatest = BetaTest.objects.filter(release = release_id)
   betatest.delete()

   return redirect('apps.devproc.views.release.view_all_releases')   

