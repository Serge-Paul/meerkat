from django.http import HttpResponse


def view_all_usecases(request):
   return HttpResponse("Hello, world. You're viewing all usecases")

def create_usecase(request):
   return HttpResponse("You're adding new usecase")

def view_usecase(request, usecase_id):
   return HttpResponse("You're looking at usecase %s." % usecase_id)

def edit_usecase(request, usecase_id):
   return HttpResponse("You're editing usecase %s." % usecase_id)

