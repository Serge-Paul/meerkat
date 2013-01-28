from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class MemberForm(forms.Form):
   first_name = forms.CharField(max_length=200)
   last_name = forms.CharField(max_length=200)
   title = forms.CharField(max_length=200, required=False)
   team = forms.ModelMultipleChoiceField(queryset=Team.objects.all()) 
   is_manager = forms.BooleanField(default=False)


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

                                                           
