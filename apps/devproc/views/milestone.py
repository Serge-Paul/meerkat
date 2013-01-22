from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_milestones(request):
   milestone_list = Milestone.objects.all().order_by('-id')
   return render_to_response('milestones/view_all_milestones.html', {'milestone_list': milestone_list})


def create_milestone(request):
   return HttpResponse("You're adding new milestone")

def view_milestone(request, milestone_id):
   milestone = Milestone.objects.get(id = milestone_id)
   return render_to_response('milestones/view_milestone.html', {'milestone': milestone})


def edit_milestone(request, milestone_id):
   return HttpResponse("You're editing milestone %s." % milestone_id)


def delete_milestone(request, milestone_id):

   milestone = Milestone.objects.get(id = milestone_id)
   milestone.delete()

   return redirect('apps.devproc.views.milestone.view_all_milestones')   
                                                              
