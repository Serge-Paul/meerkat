from django import forms
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext


class LoginForm(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(max_length=100, widget=forms.PasswordInput)
  next = forms.CharField(max_length=255, widget=forms.HiddenInput, required=False, initial="/")


def process_login(request):

  if request.method == 'POST':
    form = LoginForm(request.POST)

    if(form.is_valid()):
      user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])

      if user is not None:
        if user.is_active:
          login(request, user)

          if( request.REQUEST.get('next',None) != None ):
            return redirect(request.REQUEST.get('next','/'))

          return redirect("/")

      else:
        # User could not be authenticated
        message = "Invalid email address or password. Please try again."
        return render_to_response('registration/login.html', {'form' : form, 'message' : error_message}, context_instance=RequestContext(request))
    else:
      return render_to_response('registration/login.html', {'form' : form}, context_instance=RequestContext(request))

  else:
    defaults = { 'next' : request.REQUEST.get('next','/') }
    form = LoginForm(initial=defaults)
    return render_to_response('registration/login.html', {'form' : form}, context_instance=RequestContext(request))

def process_logout(request):
  logout(request)
  return redirect('apps.public.views.frontend.index')

