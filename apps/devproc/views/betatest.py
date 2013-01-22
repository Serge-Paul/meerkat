from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_betatests(request):
   betatest_list = BetaTest.objects.all().order_by('-id')
   return render_to_response('betatests/view_all_betatests.html', {'betatest_list': betatest_list})


def create_betatest(request):
   return HttpResponse("You're adding new betatest")

def view_betatest(request, betatest_id):
   betatest = BetaTest.objects.get(id = betatest_id)
   return render_to_response('betatests/view_betatest.html', {'betatest': betatest})


def edit_betatest(request, betatest_id):
   return HttpResponse("You're editing betatest %s." % betatest_id)

def delete_betatest(request, betatest_id):

   betatest = BetaTest.objects.get(id = betatest_id)
   betatest.delete()

   return redirect('apps.devproc.views.betatest.view_all_betatests')   


