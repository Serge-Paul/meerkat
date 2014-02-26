import os
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# CHOICES = (('display_text', 'database_text'), )
# database_text is shown in select menus

APPROVAL_STATUS_CHOICES = (
   ('Approved', 'Approved'),
   ('Rejected', 'Rejected'),
   ('Pending', 'Pending'),
)

PRIORITY_CHOICES = (
   ('Low', 'Low'),
   ('Medium', 'Medium'),
   ('High', 'High'),
   ('Critical', 'Critical'),
)

TEST_STATUS_CHOICES = (
   ('Pass', 'Pass'),
   ('Fail', 'Fail'),
   ('Pending', 'Pending'),
)

BUG_STATUS_CHOICES = (
   ('Open', 'Open'),
   ('Closed', 'Closed'),
   ('Deferred', 'Deferred'),
   ('Duplicate', 'Duplicate'),
)

PROBABILITY_CHOICES = (
   ('Very Low', 'Very Low'),
   ('Low', 'Low'),
   ('Medium', 'Medium'),
   ('High', 'High'),
   ('Very High', 'Very High'),
)

RISK_CHOICES = (
   ('Open', 'Open'),
   ('Resolved', 'Resolved'),
)

SOURCE_CHOICES = (
   ('Customer', 'Customer'),
   ('Internal', 'Internal'),
) 

RESPONSIBILITY_CHOICES = (
   ('Use Cases','Use Cases'),
   ('Requirements','Requirements'),
   ('Design','Design'),
   ('Features','Features'),
   ('Tests','Tests'),
   ('Bugs','Bugs'),
   ('Beta Tests','Beta Tests'),
)


class FileAttachment(models.Model):

   def attachment_path(instance, filename):
     return os.path.join('uploaded_attachments', 'companyID_' + str(instance.company.id), 'userID_' + str(instance.id) + '_' + filename)

   filename = models.CharField(max_length=200)
   url = models.URLField()
   delete_url = models.URLField()
   requirement = models.ForeignKey('Requirement', blank=True, null=True)
   file = models.FileField(upload_to=attachment_path, default='default_profile_photo.png',blank=True, null=True)
   company = models.ForeignKey('Company')

class UserProfile(models.Model): 

   def profile_photo_path(instance, filename):
     return os.path.join('profile_photos', 'companyID_' + str(instance.company.id), 'userID_' + str(instance.id) + '_' + filename)

   user = models.OneToOneField(User) # user object has firstname, lastname, and email
   title = models.CharField(max_length=200, blank=True, null=True)
   team = models.ManyToManyField('Team')
   is_manager = models.BooleanField(default=False)
   photo = models.FileField(upload_to=profile_photo_path, default='default_profile_photo.png',blank=True, null=True)
   #permissions
   company = models.ForeignKey('Company')

   def __unicode__(self):
      return self.user.first_name


# Add an extra attribute called profile to the User object.
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Company(models.Model):

   def company_logo_path(instance, filename):
     return os.path.join('company_logos', 'companyID_' + str(instance.id), 'companyID_' + str(instance.id) + filename)

   name = models.CharField(max_length=200)
   admin = models.ForeignKey(User)
   logo = models.FileField(upload_to=company_logo_path, default='default_company_logo.png')

   def __unicode__(self):
      return self.name


class Product(models.Model):
   name = models.CharField(max_length=200)
   description = models.TextField(max_length=1028)
   company = models.ForeignKey('Company')

   def __unicode__(self):
      return self.name


class Category(models.Model):
   category = models.CharField(max_length=200)
   
   def __unicode__(self):
      return self.category


class Requirement(models.Model): 
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   category = models.ManyToManyField(Category, blank=True, null=True) 
   parent = models.ForeignKey("self", blank=True, null=True)  
   use_case = models.ForeignKey('UseCase', blank=True, null=True)
   priority = models.CharField(max_length=128, choices=PRIORITY_CHOICES) 
   release = models.ForeignKey('Release', blank=True, null=True) 
   approval_status = models.CharField(max_length=128, choices=APPROVAL_STATUS_CHOICES) 
   identifier = models.CharField(max_length=200)
   source = models.CharField(max_length=128, choices=SOURCE_CHOICES)
   notes = models.TextField(max_length=1028, blank=True, null=True)
   #attachments
   product = models.ForeignKey('Product')
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)

   def __unicode__(self):
      return self.title


class UseCase(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   target_market = models.CharField(max_length=200, blank=True, null=True)
   identifier = models.CharField(max_length=200)
   source = models.CharField(max_length=128, choices=SOURCE_CHOICES)
   notes = models.TextField(max_length=1028, blank=True, null=True)
   product = models.ForeignKey('Product')
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   #attachments

   def __unicode__(self):
      return self.title


class Attribute(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   component = models.ForeignKey('Component')

   def __unicode__(self):
      return self.title
  

class Component(models.Model):
   title = models.CharField(max_length=200)
   design_description = models.TextField(max_length=1028)
   implementation_description = models.TextField(max_length=1028)
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   category = models.ManyToManyField('Category', blank=True, null=True)
   #attachments
   parent = models.ForeignKey('Component', blank=True, null=True)
   release = models.ForeignKey('Release', blank=True, null=True)
   approval_status = models.CharField(max_length=128, choices=APPROVAL_STATUS_CHOICES)
   identifier = models.CharField(max_length=200)
   notes = models.TextField(max_length=1028, blank=True, null=True)
   requirements = models.ManyToManyField('Requirement', blank=True, null=True)
   usecases = models.ManyToManyField('Usecase', blank=True, null=True)
   product = models.ForeignKey('Product')

   def __unicode__(self):
      return self.title


class Feature(models.Model):
   title = models.CharField(max_length=200)
   design_description = models.TextField(max_length=1028)
   implementation_description = models.TextField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   #attachments
   #implementation
   release = models.ForeignKey('Release')
   approval_status = models.CharField(max_length=128, choices=APPROVAL_STATUS_CHOICES)
   usecases = models.ManyToManyField('UseCase', blank=True, null=True)
   requirements = models.ManyToManyField('Requirement', blank=True, null=True)
   identifier = models.CharField(max_length=200)
   notes = models.TextField(max_length=1028, blank=True, null=True) 
   component = models.ManyToManyField('Component', blank=True, null=True)
   product = models.ForeignKey('Product')
   start_date = models.DateTimeField(default=datetime.now)
   end_date = models.DateTimeField()

   def __unicode__(self):
      return self.title


class Test(models.Model):
   title = models.CharField(max_length=200)
   test_description = models.TextField(max_length=1028, blank=True, null=True)
   implementation_description = models.TextField(max_length=1028, blank=True, null=True)
   category = models.ManyToManyField('Category', blank=True, null=True)
   features = models.ManyToManyField('Feature', blank=True, null=True)
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   pass_fail_criteria = models.CharField(max_length=1028, blank=True, null=True)
   status = models.CharField(max_length=128, choices=TEST_STATUS_CHOICES)
   identifier = models.CharField(max_length=200)
   #attachments
   product = models.ForeignKey('Product')
   notes = models.TextField(max_length=1028, blank=True, null=True)

   def __unicode__(self):
      return self.title


class Bug(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField(max_length=1028)
   features = models.ManyToManyField(Feature, blank=True, null=True)
   severity = models.CharField(max_length=128, choices=PRIORITY_CHOICES)
   status = models.CharField(max_length=128, choices=BUG_STATUS_CHOICES)
   release = models.ForeignKey('Release', blank=True, null=True)
   test = models.ForeignKey('Test', blank=True, null=True)
   identifier = models.CharField(max_length=200)
   category = models.ManyToManyField('Category', blank=True, null=True)
   #attachments
   resolution = models.TextField(max_length=1028, blank=True, null=True)
   betatest = models.ForeignKey('BetaTest', blank=True, null=True)
   notes = models.TextField(max_length=1028, blank=True, null=True)

   def __unicode__(self):
      return self.title


class BetaTest(models.Model):
   release = models.OneToOneField('Release')
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)

   def __unicode__(self):
      return self.release.name  #might want to change this


class Customer(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200) 
   organization = models.CharField(max_length=200)
   location = models.CharField(max_length=200, blank=True, null=True) 
   company = models.ForeignKey('Company')

   def __unicode__(self):
      return self.first_name


class Feedback(models.Model):
   betatest = models.ForeignKey('BetaTest')
   customer = models.ForeignKey('Customer')
   feature = models.ForeignKey('Feature')
   feedback = models.TextField(max_length=1028)

   def __unicode__(self):
      return self.feedback


class Release(models.Model):
   name = models.CharField(max_length=200)
   release_date = models.DateTimeField()
   pass_fail_criteria = models.CharField(max_length=1028, blank=True, null=True)
   market = models.CharField(max_length=200, blank=True, null=True) #maybe define class for market
   #documents
   #marketing_documents
   #press_release_documents
   notes = models.TextField(max_length=1028, blank=True, null=True)
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True, related_name='responsible_engineer')
   goals = models.CharField(max_length=1028, blank=True, null=True)
   product = models.ForeignKey('Product')
   product_manager = models.ManyToManyField('Member', blank=True, null=True, related_name='product_manager')

   def __unicode__(self):
      return self.name


class Risk(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   probability = models.CharField(max_length=128, choices=PROBABILITY_CHOICES)
   severity = models.CharField(max_length=128, choices=PRIORITY_CHOICES)
   status = models.CharField(max_length=128, choices=RISK_CHOICES)
   identifier = models.CharField(max_length=200)
   #attachment
   feature = models.ForeignKey('Feature', blank=True, null=True)
   bug = models.ForeignKey('Bug', blank=True, null=True)
   component = models.ForeignKey('Component', blank=True, null=True)
   notes = models.TextField(max_length=1028, blank=True, null=True)

   def __unicode__(self):
      return self.title


class Responsibility(models.Model):
   responsibility = models.CharField(max_length=128, choices=RESPONSIBILITY_CHOICES)
   team = models.ForeignKey('Team')
   release = models.ForeignKey('Release')

   def __unicode__(self):
      return self.responsibility


class Team(models.Model):

   def team_logo_path(instance, filename):
     return os.path.join('team_logos', 'companyID_' + str(instance.company.id), 'teamID_' + str(instance.id) + '_' + filename)


   #manager = models.ForeignKey('Member')
   name = models.CharField(max_length=200)
   logo = models.FileField(upload_to=team_logo_path, default='default_team_logo.png',blank=True, null=True)
   description = models.TextField(max_length=1028, blank=True, null=True)
   company = models.ForeignKey('Company')
   products = models.ManyToManyField('Product')

   def __unicode__(self):
      return self.name


class Member(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   title = models.CharField(max_length=200, blank=True, null=True)
   team = models.ManyToManyField('Team')
   is_manager = models.BooleanField(default=False)
   #photo
   #permissions
   company = models.ForeignKey('Company')

   def __unicode__(self):
      return self.first_name


class Milestone(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   #phase
   start_date = models.DateTimeField(default=datetime.now)
   end_date = models.DateTimeField()
   release = models.ForeignKey('Release')
   predecessors = models.ManyToManyField('Milestone', blank=True, null=True)
   percent_complete = models.IntegerField()
   notes = models.TextField(max_length=1028, blank=True, null=True) 
   product = models.ForeignKey('Product')

   def __unicode__(self):
      return self.title


