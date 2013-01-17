from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_attributes(request, component_id):
   # View all attributes associates with a specific component
 
   attribute_list = Attribute.objects.all().order_by('-id')
   return render_to_response('attributes/view_all_attributes.html', {'attribute_list': attribute_list})
 

def create_attribute(request):
   return HttpResponse("You're adding new attribute")

def view_attribute(request, component_id, attribute_id):
   attribute = Attribute.objects.get(id = attribute_id)
   component = Component.objects.get(id = component_id)
   return render_to_response('attributes/view_attribute.html', {'attribute': attribute, 'component': component})


def edit_attribute(request, attribute_id):
   return HttpResponse("You're editing attribute %s." % attribute_id)
