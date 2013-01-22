from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_bugs(request):
   bug_list = Bug.objects.all().order_by('-id')
   return render_to_response('bugs/view_all_bugs.html', {'bug_list': bug_list})


def create_bug(request):
   return HttpResponse("You're adding new bug")

def view_bug(request, bug_id):
   bug = Bug.objects.get(id = bug_id)
   return render_to_response('bugs/view_bug.html', {'bug': bug})


def edit_bug(request, bug_id):
   return HttpResponse("You're editing bug %s." % bug_id)

def delete_bug(request, bug_id):

   bug = Bug.objects.get(id = bug_id)
   bug.delete()

   return redirect('apps.devproc.views.bug.view_all_bugs')   
                                                         
