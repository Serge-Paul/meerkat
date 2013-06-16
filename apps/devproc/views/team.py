from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


class TeamForm(forms.Form):
   team_name = forms.CharField(max_length=250) 
   description= forms.CharField(max_length=1028, widget=forms.Textarea, required=False)
   responsibility = forms.ChoiceField(choices=RESPONSIBILITY_CHOICES)
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=True) 


@login_required
def view_all_teams(request):
   session_info = get_session_info(request)

   team_list = Team.objects.all().order_by('-id')
   return render_to_response('teams/view_all_teams.html', {'session_info': session_info, 'user' : request.user, 'team_list': team_list})


@login_required
def create_team(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = TeamForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         team = Team()
         team.name = form.cleaned_data['team_name']
         team.description = form.cleaned_data['description']
         team.company = request.user.profile.company
         team.save()

         responsibility = Responsibility()
         responsibility.release = form.cleaned_data['release']
         responsibility.team = team
         responsibility.responsibility = form.cleaned_data['responsibility'] 
         responsibility.save()
 
         return redirect('apps.devproc.views.team.view_team', team_id = team.id)
    
      else: #if form is not valid
          return render_to_response('teams/create_team.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating team. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = TeamForm()
      return render_to_response('teams/create_team.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_team(request, team_id):
   session_info = get_session_info(request)

   team = Team.objects.get(id = team_id)
   members = Member.objects.filter(team = team_id)
   responsibilities = Responsibility.objects.filter(team = team_id)

   return render_to_response('teams/view_team.html', {'session_info': session_info, 'user' : request.user, 'team': team, 'members': members, 'responsibilities': responsibilities})


@login_required
def edit_team(request, team_id):
   session_info = get_session_info(request)
   
   team = Team.objects.get(id = team_id)
   responsibility = Responsibility.objects.get(team = team_id)

   if request.method == 'POST':
  
      form = TeamForm(request.POST)
  
      # Do when form is submitted
      if form.is_valid():

         team.name = form.cleaned_data['team_name']
         team.description = form.cleaned_data['description']
         team.save()

         responsibility.release = form.cleaned_data['release']
         responsibility.responsibility = form.cleaned_data['responsibility']
         responsibility.save()

         return redirect('apps.devproc.views.team.view_team', team_id = team.id)
    
      else: #if form is not valid 
          return render_to_response('teams/create_team.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing team. Please try again.', 'team': team, 'mode': 'edit'}, context_instance=RequestContext(request))

   else: #code for just initially displaying form
      
      defaults = { 
                 'team_name' : team.name, 
                 'description': team.description,
                 'responsibility': responsibility.responsibility,
                 'release': responsibility.release,
                 }

      form = TeamForm(initial=defaults)   
 
      return render_to_response('teams/create_team.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'team': team, 'mode': 'edit' },  context_instance=RequestContext(request))


@login_required
def delete_team(request, team_id):
   session_info = get_session_info(request)
   
   team = Team.objects.get(id = team_id)
   team.delete()

   return redirect('apps.devproc.views.team.view_all_teams')   


