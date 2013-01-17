from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_roadmaps(request):
   roadmap_list = Roadmap.objects.all().order_by('-id')
   return render_to_response('roadmaps/view_all_roadmaps.html', {'roadmap_list': roadmap_list})


def create_roadmap(request):
   return HttpResponse("You're adding new roadmap")

def view_roadmap(request, roadmap_id):
   roadmap = Roadmap.objects.get(id = roadmap_id)
   return render_to_response('roadmaps/view_roadmap.html', {'roadmap': roadmap})


def edit_roadmap(request, roadmap_id):
   return HttpResponse("You're editing roadmap %s." % roadmap_id)

