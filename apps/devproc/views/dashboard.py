from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


@login_required
def view_dashboard(request):
  session_info = get_session_info(request)

  return render_to_response('dashboard/view_dashboard.html', {'session_info': session_info, 'user': request.user}, context_instance=RequestContext(request))


