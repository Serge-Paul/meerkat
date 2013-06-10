from apps.devproc.models import *
import binascii
import uuid
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


# Generates a 25 character base64 encoded UUID. To get the original UUID you can do
# uuid.UUID(bytes=binascii.a2b_base64(uuid_b64))
def base64_uuid():
  x = uuid.uuid4()
  uuid_b64 = binascii.b2a_base64(x.bytes)
  return uuid_b64


def new_user(email, password, first_name="", last_name=""):

  if( User.objects.filter(email=email).count() == 0 ):  #if user does not exist in database
    user = User.objects.create_user( base64_uuid(), email, password)
    user.first_name = first_name
    user.last_name = last_name
    profile = user.profile
    profile.save()
    user.save()
    log.debug("Created new user: %s" % email)
  else:  #if user already exists in database
    user = User.objects.get(email=email)
    if( user.is_active == False ):
      user.set_password(password)
      user.is_active = True
      user.first_name = first_name
      user.last_name = last_name
      profile = user.profile
      profile.save()
      user.save()
  return user


def send_welcome_email(email):
   user = User.objects.get(email=email)

   current_site = Site.objects.get_current()

   html_content = render_to_string('emails/new_registration_email.html', {'email' : email, 'site_url' : 'http://%s/' % current_site.domain, 'name' : user.first_name })

   text_content = strip_tags(html_content) # this strips the html, so people will have the text as well.

   # create the email, and attach the HTML version as well.
   email = EmailMultiAlternatives('Welcome to Meerkat!', text_content, 'Meerkate <info@meerkatdev.com>',
                [email], ['info@meerkatdev.com'], headers = {'Reply-To': settings.DEFAULT_FROM_EMAIL})

   email.attach_alternative(html_content, "text/html")

   email.send(fail_silently = False)

   log.debug("Sent welcome email to %s" % email)


