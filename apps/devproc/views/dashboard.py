from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def view_dashboard(request):

  return render_to_response('dashboard/view_dashboard.html', {'user' : request.user}, context_instance=RequestContext(request))


