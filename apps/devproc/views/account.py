from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


class AccountForm(forms.Form):
   first_name = forms.CharField(label="First name", max_length=256) 
   last_name = forms.CharField(label="Last name", max_length=256)
   username = forms.CharField(label="Username", max_length=256)
   email = forms.EmailField(label="Email")
   photo = forms.FileField()

@login_required
def view_account(request):
   session_info = get_session_info(request)

   return render_to_response('account/view_account.html', {'session_info': session_info, 'user' : request.user}, context_instance=RequestContext(request))
  

@login_required
def edit_account(request):
   session_info = get_session_info(request)

   if request.method == 'POST':
  
      form = AccountForm(request.POST, request.FILES)
  
      # Do when form is submitted
      if form.is_valid():

         request.user.first_name = form.cleaned_data['first_name']
         request.user.last_name = form.cleaned_data['last_name']
         request.user.username = form.cleaned_data['username']
         request.user.email = form.cleaned_data['email']
 
         file = request.FILES['photo'] 

         request.user.profile.photo.save(file.name, file, save=True)

         request.user.profile.save()    
         request.user.save()

         return redirect('apps.devproc.views.account.view_account')
    
      else: #if form is not valid 
          return render_to_response('account/edit_account.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing account. Please try again.'}, context_instance=RequestContext(request))

   else: #code for just initially displaying form
      
      defaults = { 
                 'first_name' : request.user.first_name, 
                 'last_name': request.user.last_name,
                 'username': request.user.username,
                 'email': request.user.email,
                 }

      form = AccountForm(initial=defaults)   
 
      return render_to_response('account/edit_account.html', {'session_info': session_info, 'user' : request.user, 'form': form},  context_instance=RequestContext(request))






