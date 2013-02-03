from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required


@login_required
def view_roadmap(request): 
   #right now just showing all releases, but later need to only select releases for the current product account
   releases = Release.objects.all().order_by('-id')
   features = Feature.objects.all()
   return render_to_response('roadmaps/roadmap.html', {'releases': releases, 'features': features})

