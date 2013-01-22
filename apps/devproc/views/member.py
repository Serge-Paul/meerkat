from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_members(request, team_id):
   # view all members for a specific team
   member_list = Member.objects.all().order_by('-id')

   team = Team.objects.get(id = team_id)   

   return render_to_response('members/view_all_members.html', {'member_list': member_list, 'team': team})


def create_member(request, team_id):
   # create a new member and add them to a specific team
   return HttpResponse("You're adding new member")

def view_member(request, member_id):
   member = Member.objects.get(id = member_id)
   return render_to_response('members/view_member.html', {'member': member})


def edit_member(request, member_id):
   return HttpResponse("You're editing member %s." % member_id)   


def delete_member(request, member_id):

   member = Member.objects.get(id = member_id)
   member.delete()

   return redirect('apps.devproc.views.member.view_all_members')   

                                                           
