from apps.devproc.models import *
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponse
from django.utils import simplejson

def delete_file(request):
   if request.method == 'POST':
        data = {}
        file_path = request.POST['file_path']

        attachment = FileAttachment.objects.filter(url = file_path)
     
        #attachment.file.storage.delete(attachment.file.path)

        data['message'] = "The file has been deleted: " + attachment.filename

        return HttpResponse(simplejson.dumps(data), mimetype="application/json")
       


def get_session_info(request):
   company = request.user.profile.company

   products = Product.objects.filter(company = company.id)

   active_product = request.session.get('active_product')

   session_info = {
                   'company': company,
                   'products': products,
                   'active_product': active_product,
                  } 

   return session_info


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

   html_content = render_to_string('emails/new_registration_email.html', {'site_url' : 'http://%s/' % current_site.domain, 'name' : user.first_name })

   text_content = strip_tags(html_content) # this strips the html, so people will have the text as well.

   # create the email, and attach the HTML version as well.
   email = EmailMultiAlternatives('Welcome to Meerkat!', text_content, 'Meerkat <info@meerkatdev.com>',
                [email], ['info@meerkatdev.com'], headers = {'Reply-To': settings.DEFAULT_FROM_EMAIL})

   email.attach_alternative(html_content, "text/html")

   email.send(fail_silently = False)

   


