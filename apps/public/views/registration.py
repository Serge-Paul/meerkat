from apps.devproc.models import *
from apps.devproc.utils import *
from django import forms

from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


class RegistrationForm(forms.Form):

  first_name = forms.CharField(label="First name", max_length=256)
  last_name = forms.CharField(label="Last name", max_length=256)
  email = forms.EmailField(label="Email")
  password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
  confirm_password = forms.CharField(label="Confirm password", max_length=100, widget=forms.PasswordInput)
  company = forms.CharField(label="Company or Project Name", max_length=256)
  username =  = forms.CharField(label="Username", max_length=256)

  # Return errr if user tries to signup and already has an active account
  def clean_email(self):
    email = self.cleaned_data['email']
    email = email.lower()

    if( User.objects.filter(email=email).count() != 0 ):
      raise forms.ValidationError("That email address has already been taken.")

    return email

  def clean_confirm_password(self):
    password = self.cleaned_data['password']
    confirm_password = self.cleaned_data['confirm_password']

    if( password != confirm_password ):
      raise forms.ValidationError("Passwords do not match.")
    return confirm_password


def account_registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)

    if(form.is_valid() == False):
      return render_to_response('registration/registration.html', {'form':form}, context_instance=RequestContext(request))

    # Look to see if there is an user object already created for the email. 
  
   
    #user = User.objects.create_user( base64_uuid(), form.cleaned_data['email'], form.cleaned_data['password'])
    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])


    user.first_name = form.cleaned_data['first_name']
    user.last_name = form.cleaned_data['last_name']
    user.save()

    company = Company()
    company.name = form.cleaned_data['company']
    company.admin = user
    company.save()

    profile = UserProfile()
    profile.company = company
    profile.user = user
    profile.save()


    # Send welcome email to the user

    send_welcome_email(form.cleaned_data['email'])

    # Log the user in (saves the user's ID in the session)
    #user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
    user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
  
    login(request, user)

    return render_to_response('registration/registration_success.html', {}, context_instance=RequestContext(request))

  else:
    if request.user.is_authenticated():
      return redirect('apps.devproc.views.public.index')
    else:

      form = RegistrationForm()

      return render_to_response('registration/registration.html', {'form': form }, context_instance=RequestContext(request))


