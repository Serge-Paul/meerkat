from django.http import HttpResponse


def view_all_roadmaps(request):
   return HttpResponse("Hello, world. You're viewing all roadmaps")

def create_roadmap(request):
   return HttpResponse("You're adding new roadmap")

def view_roadmap(request, roadmap_id):
   return HttpResponse("You're looking at roadmap %s." % roadmap_id)

def edit_roadmap(request, roadmap_id):
   return HttpResponse("You're editing roadmap %s." % roadmap_id)

