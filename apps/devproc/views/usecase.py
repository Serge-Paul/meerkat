from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_usecases(request):
   usecase_list = UseCase.objects.all().order_by('-id')
   return render_to_response('usecases/view_all_usecases.html', {'usecase_list': usecase_list})


def create_usecase(request):
   return HttpResponse("You're adding new usecase")

def view_usecase(request, usecase_id):
   return HttpResponse("You're looking at usecase %s." % usecase_id)

def edit_usecase(request, usecase_id):
   return HttpResponse("You're editing usecase %s." % usecase_id)

