from django.http import HttpResponse


def view_all_components(request):
   return HttpResponse("Hello, world. You're viewing all components")

def create_component(request):
   return HttpResponse("You're adding new component")

def view_component(request, component_id):
   return HttpResponse("You're looking at component %s." % component_id)

def edit_component(request, component_id):
   return HttpResponse("You're editing component %s." % component_id)
                                                             
