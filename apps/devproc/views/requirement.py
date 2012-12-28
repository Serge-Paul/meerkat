from django.http import HttpResponse


def view_all_reqmts(request): 
   return HttpResponse("Hello, world. You're viewing all reqmts")

def create_reqmt(request):
   return HttpResponse("You're adding new reqmt")

def view_reqmt(request, reqmt_id):
   return HttpResponse("You're looking at reqmt %s." % reqmt_id)

def edit_reqmt(request, reqmt_id):
   return HttpResponse("You're editing reqmt %s." % reqmt_id)
