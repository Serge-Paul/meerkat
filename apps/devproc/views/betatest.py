from django.http import HttpResponse


def view_all_betatests(request):
   return HttpResponse("Hello, world. You're viewing all betatests")

def create_betatest(request):
   return HttpResponse("You're adding new betatest")

def view_betatest(request, betatest_id):
   return HttpResponse("You're looking at betatest %s." % betatest_id)

def edit_betatest(request, betatest_id):
   return HttpResponse("You're editing betatest %s." % betatest_id)
