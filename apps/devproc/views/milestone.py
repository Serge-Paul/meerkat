from django.http import HttpResponse


def view_all_milestones(request):
   return HttpResponse("Hello, world. You're viewing all milestones")

def create_milestone(request):
   return HttpResponse("You're adding new milestone")

def view_milestone(request, milestone_id):
   return HttpResponse("You're looking at milestone %s." % milestone_id)

def edit_milestone(request, milestone_id):
   return HttpResponse("You're editing milestone %s." % milestone_id)
                                                              
