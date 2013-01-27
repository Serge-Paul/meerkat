from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class TeamForm(forms.Form):
   team_name = forms.CharField(max_length=250) 

def view_all_teams(request):
   team_list = Team.objects.all().order_by('-id')
   return render_to_response('teams/view_all_teams.html', {'team_list': team_list})


def create_team(request):
   if request.method == 'POST':

      form = TeamForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         team = Team()
         team.name = form.cleaned_data['team_name']
         team.save()

         return redirect('apps.devproc.views.team.view_team', team_id = team.id)
    
      #else: #if form is not valid

   else: #code for just initially displaying form
      form = TeamForm()
      return render_to_response('teams/create_team.html', {'form': form},  context_instance=RequestContext(request))


def view_team(request, team_id):
   team = Team.objects.get(id = team_id)
   members = Member.objects.filter(team = team_id)
   responsibilities = Responsibility.objects.filter(team = team_id)

   return render_to_response('teams/view_team.html', {'team': team, 'members': members, 'responsibilities': responsibilities})


def edit_team(request, team_id):
   
   team = Team.objects.get(id = team_id)

   if request.method == 'POST':
  
      form = TeamForm(request.POST)
  
      # Do when form is submitted
      if form.is_valid():

         team.name = form.cleaned_data['team_name']
         team.save()

         return redirect('apps.devproc.views.team.view_team', team_id = team.id)
    
      #else: #if form is not valid

   else: #code for just initially displaying form
      
      defaults = { 'team_name' : team.name }
      form = TeamForm(initial=defaults)   
 
      return render_to_response('teams/edit_team.html', {'form': form, 'team': team },  context_instance=RequestContext(request))


def delete_team(request, team_id):
   
   team = Team.objects.get(id = team_id)
   team.delete()

   return redirect('apps.devproc.views.team.view_all_teams')   





