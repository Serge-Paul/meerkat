from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# CHOICES = (('display_text', 'database_text'), )

APPROVAL_STATUS_CHOICES = (
   ('Approved', 'approved'),
   ('Rejected', 'rejected'),
   ('Pending', 'pending'),
)

PRIORITY_CHOICES = (
   ('Low', 'low'),
   ('Medium', 'medium'),
   ('High', 'high'),
   ('Critical', 'critical'),
)

TEST_STATUS_CHOICES = (
   ('Pass', 'pass'),
   ('Fail', 'fail'),
   ('Pending', 'pending'),
)

BUG_STATUS_CHOICES = (
   ('Open', 'open'),
   ('Closed', 'closed'),
   ('Deferred', 'deferred'),
)

PROBABILITY_CHOICES = (
   ('Very Low', 'very_low'),
   ('Low', 'low'),
   ('Medium', 'medium'),
   ('High', 'high'),
   ('Very High', 'very_high'),
)

RISK_CHOICES = (
   ('Open', 'open'),
   ('Resolved', 'resolved'),
)

SOURCE_CHOICES = (
   ('Customer', 'customer'),
   ('Internal', 'internal'),
) 

RESPONSIBILITY_CHOICES = (
   ('Use Cases','usecase'),
   ('Requirements','reqmt'),
   ('Design','component'),
   ('Features','feature'),
   ('Tests','test'),
   ('Bugs','bug'),
   ('Beta Tests','betatest'),
)


class UserProfile(models.Model): 
   user = models.OneToOneField(User) # user object has firstname, lastname, and email
   title = models.CharField(max_length=200, blank=True, null=True)
   team = models.ManyToManyField('Team')
   is_manager = models.BooleanField(default=False)
   #photo
   #permissions
   company = models.ForeignKey('Company')

   def __unicode__(self):
      return self.user.first_name


# Add an extra attribute called profile to the User object.
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Company(models.Model):
   name = models.CharField(max_length=200)
   admin = models.ForeignKey(User)

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
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   goals = models.CharField(max_length=1028, blank=True, null=True)
   product = models.ForeignKey('Product')

   def __unicode__(self):
      return self.name


class Risk(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   release = models.ForeignKey('Release', blank=True, null=True)
   probability = models.CharField(max_length=128, choices=PROBABILITY_CHOICES)
   severity = models.CharField(max_length=128, choices=PRIORITY_CHOICES)
   status = models.CharField(max_length=128, choices=RISK_CHOICES)
   identifier = models.CharField(max_length=200)
   #attachment
   approval_status = models.CharField(max_length=128, choices=APPROVAL_STATUS_CHOICES)
   feature = models.ForeignKey('Feature', blank=True, null=True)
   bug = models.ForeignKey('Bug', blank=True, null=True)
   component = models.ForeignKey('Component', blank=True, null=True)

   def __unicode__(self):
      return self.title


class Responsibility(models.Model):
   responsibility = models.CharField(max_length=128, choices=RESPONSIBILITY_CHOICES)
   team = models.ForeignKey('Team')
   release = models.ForeignKey('Release')

   def __unicode__(self):
      return self.responsibility


class Team(models.Model):
   #manager = models.ForeignKey('Member')
   name = models.CharField(max_length=200)
   #logo
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


