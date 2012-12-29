from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_teams(request):
   team_list = Team.objects.all().order_by('-id')
   return render_to_response('teams/view_all_teams.html', {'team_list': team_list})


def create_team(request):
   return HttpResponse("You're adding new team")

def view_team(request, team_id):
   return HttpResponse("You're looking at team %s." % team_id)

def edit_team(request, team_id):
   return HttpResponse("You're editing team %s." % team_id)

