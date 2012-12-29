from django.http import HttpResponse
from django.shortcuts import render_to_response 
from apps.devproc.models import *

def view_all_reqmts(request): 
   reqmt_list = Requirement.objects.all().order_by('-id') 
   return render_to_response('requirements/view_all_reqmts.html', {'reqmt_list': reqmt_list})

def create_reqmt(request):
   return HttpResponse("You're adding new reqmt")

def view_reqmt(request, reqmt_id):
   reqmt = Requirement.objects.get(id = reqmt_id)
   return render_to_response('requirements/view_reqmt.html', {'reqmt': reqmt})

  

def edit_reqmt(request, reqmt_id):
   return HttpResponse("You're editing reqmt %s." % reqmt_id)
