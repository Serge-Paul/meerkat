from django.http import HttpResponse


def view_all_teams(request):
   return HttpResponse("Hello, world. You're viewing all teams")

def create_team(request):
   return HttpResponse("You're adding new team")

def view_team(request, team_id):
   return HttpResponse("You're looking at team %s." % team_id)

def edit_team(request, team_id):
   return HttpResponse("You're editing team %s." % team_id)

