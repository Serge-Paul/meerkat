from apps.devproc.models import *
from django import forms
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext
from django.contrib.auth import authenticate, login, logout
from apps.devproc.utils import *


class LoginForm(forms.Form):
  username = forms.CharField(max_length=255)
  password = forms.CharField(max_length=100, widget=forms.PasswordInput)
  next = forms.CharField(max_length=255, widget=forms.HiddenInput, required=False, initial="/")

def process_login(request):

  if request.method == 'POST':
    form = LoginForm(request.POST)

    if(form.is_valid()):
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

      if user is not None:
       # if user.is_active:
        login(request, user)

        active_product = Product.objects.filter(company = request.user.profile.company.id)[0]

        request.session['active_product'] = active_product
        request.session.save()
  
        session_info = get_session_info(request)

        if request.REQUEST.get('next',None) == '/': 
 
          return render_to_response('dashboard/view_dashboard.html', {'session_info': session_info, 'user': request.user}, context_instance=RequestContext(request))

        else:
           return redirect(request.REQUEST.get('next','/'))
      

      else:
        # User could not be authenticated
        message = "Invalid username or password. Please try again."
        return render_to_response('registration/login.html', {'form' : form, 'message' : message}, context_instance=RequestContext(request))

    else: #if form is not valid
      return render_to_response('registration/login.html', {'form' : form}, context_instance=RequestContext(request))

  else:  # displaying blank form for the first time
    defaults = { 'next' : request.REQUEST.get('next','/') }
    form = LoginForm(initial=defaults)
    return render_to_response('registration/login.html', {'form' : form}, context_instance=RequestContext(request))

def process_logout(request):
  logout(request)
  return redirect('apps.public.views.auth.process_login')











      


 








 


