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

   releases = Release.objects.filter(product = session_info['active_product']).order_by('-id')
   features = Feature.objects.filter(product = session_info['active_product']).order_by('-id')

   return render_to_response('roadmaps/roadmap.html', {'session_info': session_info, 'user' : request.user, 'releases': releases, 'features': features})

