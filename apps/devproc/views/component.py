from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_components(request):
   component_list = Component.objects.all().order_by('-id')
   return render_to_response('components/view_all_components.html', {'component_list': component_list})


def create_component(request):
   return HttpResponse("You're adding new component")

def view_component(request, component_id):
  component = Component.objects.get(id = component_id)
  return render_to_response('components/view_component.html', {'component': component})


def edit_component(request, component_id):
   return HttpResponse("You're editing component %s." % component_id)


def delete_component(request, component_id):

   component = Component.objects.get(id = component_id)
   component.delete()

   return redirect('apps.devproc.views.component.view_all_components')   
                                                             
