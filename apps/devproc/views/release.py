from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class ReleaseForm(forms.Form):
   name = forms.CharField(max_length=200)
   release_date = forms.DateField()
   pass_fail_criteria = forms.CharField(max_length=1028, required=False)
   market = forms.CharField(max_length=200, required=False)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)  
   responsible_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False) 
   goals = forms.CharField(max_length=1028, required=False)


def view_all_releases(request):
   release_list = Release.objects.all().order_by('-id')
   return render_to_response('releases/view_all_releases.html', {'release_list': release_list})


def create_release(request):
   return HttpResponse("You're adding new release")

def view_release(request, release_id):
   release = Release.objects.get(id = release_id)
   features = Feature.objects.filter(release = release_id)
   risks = Risk.objects.filter(release = release_id)
   bugs = Bug.objects.filter(release = release_id)
   milestones = Milestone.objects.filter(release = release_id)

   return render_to_response('releases/view_release.html', {'release': release,'features':features , 'risks':risks, 'bugs': bugs, 'milestones': milestones })


def edit_release(request, release_id):
   return HttpResponse("You're editing release %s." % release_id)


def delete_release(request, release_id):

   release = Release.objects.get(id = release_id)
   release.delete()

   return redirect('apps.devproc.views.release.view_all_releases')   

