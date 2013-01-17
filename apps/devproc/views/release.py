from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_releases(request):
   release_list = Release.objects.all().order_by('-id')
   return render_to_response('releases/view_all_releases.html', {'release_list': release_list})


def create_release(request):
   return HttpResponse("You're adding new release")

def view_release(request, release_id):
   release = Release.objects.get(id = release_id)
   return render_to_response('releases/view_release.html', {'release': release})


def edit_release(request, release_id):
   return HttpResponse("You're editing release %s." % release_id)

