from django.http import HttpResponse


def view_all_attributes(request):
   return HttpResponse("Hello, world. You're viewing all attributes")

def create_attribute(request):
   return HttpResponse("You're adding new attribute")

def view_attribute(request, attribute_id):
   return HttpResponse("You're looking at attribute %s." % attribute_id)

def edit_attribute(request, attribute_id):
   return HttpResponse("You're editing attribute %s." % attribute_id)
