from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required

class MemberForm(forms.Form):
   existing_member = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False)
   first_name = forms.CharField(max_length=200)
   last_name = forms.CharField(max_length=200)
   title = forms.CharField(max_length=200, required=False)
   is_manager = forms.BooleanField()


@login_required
def view_all_members(request, team_id):
   # view all members for a specific team
   member_list = Member.objects.all().order_by('-id')

   team = Team.objects.get(id = team_id)   

   return render_to_response('members/view_all_members.html', {'user' : request.user, 'member_list': member_list, 'team': team})


@login_required
def create_member(request, team_id):
   # create a new member and add them to a specific team

   team = Team.objects.get(id = team_id)

   if request.method == 'POST':

      form = MemberForm(request.POST)

      # Do when form is submitted
      if form.is_valid():
#NEED TO IMPLEMENT allowing user to choose existing members
         member = Member()
         member.first_name = form.cleaned_data['first_name']
         member.last_name = form.cleaned_data['last_name']
	 member.title = form.cleaned_data['title']
	 member.is_manager = form.cleaned_data['is_manager']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         member.save()

         member.team.add(team)

         member.save()

         return redirect('apps.devproc.views.member.view_member', member_id = member.id)

      else: #if form is not valid
         return render_to_response('members/create_member.html', {'user' : request.user, 'form':form, 'message': 'Error adding team member. Please try again.', 'team': team, 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = MemberForm()
      return render_to_response('members/create_member.html', {'user' : request.user, 'form': form, 'team': team, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_member(request, member_id):
   member = Member.objects.get(id = member_id)
   return render_to_response('members/view_member.html', {'user' : request.user, 'member': member})


@login_required
def edit_member(request, member_id):

   member = Member.objects.get(id = member_id)

   if request.method == 'POST':

      form = MemberForm(request.POST)

      # Do when form is submitted
      if form.is_valid():
#NEED TO IMPLEMENT allowing user to choose existing members

         member.first_name = form.cleaned_data['first_name']
         member.last_name = form.cleaned_data['last_name']
         member.title = form.cleaned_data['title']
         member.is_manager = form.cleaned_data['is_manager']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         member.save()

         return redirect('apps.devproc.views.member.view_member', member_id = member.id)

      else: #if form is not valid
         return render_to_response('members/create_member.html', {'user' : request.user, 'form':form, 'message': 'Error editing team member. Please try again.', 'team': member.team, 'member': member, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
   
      defaults = {
                 'first_name' : member.first_name,
                 'last_name': member.last_name,
                 'title': member.title,
                 'is_manager': member.is_manager,
                 }

      form = MemberForm(initial=defaults)

      return render_to_response('members/create_member.html', {'user' : request.user, 'form': form, 'team': team, 'member': member, 'mode': 'edit'},  context_instance=RequestContext(request))



@login_required
def delete_member(request, member_id):

   member = Member.objects.get(id = member_id)
   member.delete()

   return redirect('apps.devproc.views.member.view_all_members')   

                                                           
