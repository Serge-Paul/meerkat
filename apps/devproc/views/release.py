from django.http import HttpResponse


def view_all_releases(request):
   return HttpResponse("Hello, world. You're viewing all release")

def create_release(request):
   return HttpResponse("You're adding new release")

def view_release(request, release_id):
   return HttpResponse("You're looking at release %s." % release_id)

def edit_release(request, release_id):
   return HttpResponse("You're editing release %s." % release_id)

