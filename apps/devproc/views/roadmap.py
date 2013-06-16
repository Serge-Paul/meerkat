from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


@login_required
def view_roadmap(request): 
   session_info = get_session_info(request)

   #right now just showing all releases, but later need to only select releases for the current product account
   releases = Release.objects.all().order_by('-id')
   features = Feature.objects.all()

   return render_to_response('roadmaps/roadmap.html', {'session_info': session_info, 'user' : request.user, 'releases': releases, 'features': features})

