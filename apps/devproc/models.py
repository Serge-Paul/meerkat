from django.db import models
from datetime import datetime

APPROVAL_STATUS_CHOICES = (
   ('approved', 'Approved'),
   ('rejected', 'Rejected'),
   ('pending', 'Pending'),
)

PRIORITY_CHOICES = (
   ('low', 'Low'),
   ('medium', 'Medium'),
   ('high', 'High'),
   ('critical', 'Critical'),
)

TEST_STATUS_CHOICES = (
   ('pass', 'Pass'),
   ('fail', 'Fail'),
   ('pending', 'Pending'),
)

BUG_STATUS_CHOICES = (
   ('open', 'Open'),
   ('closed', 'Closed'),
   ('deferred', 'deferred'),
)

PROBABILITY_CHOICES = (
   ('very_low', 'Very Low'),
   ('low', 'Low'),
   ('medium', 'Medium'),
   ('high', 'High'),
   ('very_high', 'Very High'),
)

RISK_CHOICES = (
   ('open', 'Open'),
   ('resolved', 'Resolved'),
)

class Category(models.Model):
   category = models.CharField(max_length=200)

class Requirement(models.Model): 
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   category = models.ManyToManyField(Category, blank=True, null=True) 
   parent = models.ForeignKey("self", blank=True, null=True)  
   features = models.ManyToManyField('Feature', blank=True, null=True)
   tests = models.ManyToManyField('Test', blank=True, null=True)
   use_case = models.ForeignKey('UseCase', blank=True, null=True)
   priority = models.CharField(max_length=128, choices=PRIORITY_CHOICES) 
   release = models.ForeignKey('Release', blank=True, null=True) 
   approval_status = models.CharField(max_length=128, choices=APPROVAL_STATUS_CHOICES) 

class UseCase(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   features = models.ManyToManyField('Feature', blank=True, null=True)
   target_market = models.CharField(max_length=200, blank=True, null=True)
   target_user = models.CharField(max_length=200, blank=True, null=True)
   release = models.ForeignKey('Release', blank=True, null=True)

class Attribute(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)

class Component(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   category = models.ManyToManyField('Category', blank=True, null=True)
   #documents
   attributes = models.ForeignKey('Attribute', blank=True, null=True)
   parent = models.ForeignKey('Component', blank=True, null=True)
   release = models.ForeignKey('Release', blank=True, null=True)
   approval_status = models.CharField(max_length=128, choices=APPROVAL_STATUS_CHOICES)

class Feature(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   #documents
   #implementation
   release = models.ForeignKey('Release', blank=True, null=True)
   approval_status = models.CharField(max_length=128, choices=APPROVAL_STATUS_CHOICES)

class Test(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   category = models.ManyToManyField('Category', blank=True, null=True)
   features = models.ManyToManyField('Feature', blank=True, null=True)
   responsible_engineer = models.ManyToManyField('Member', blank=True, null=True)
   pass_fail_criteria = models.CharField(max_length=1028, blank=True, null=True)
   equipment = models.CharField(max_length=1028, blank=True, null=True)
   status = models.CharField(max_length=128, choices=TEST_STATUS_CHOICES)

class Bug(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=1028)
   features = models.ManyToManyField(Feature, blank=True, null=True)
   severity = models.CharField(max_length=128, choices=PRIORITY_CHOICES)
   status = models.CharField(max_length=128, choices=BUG_STATUS_CHOICES)
   release = models.ForeignKey('Release', blank=True, null=True)
   test = models.ForeignKey('Test', blank=True, null=True)

class BetaTest(models.Model):
   customer = models.ManyToManyField('Customer')
   release = models.OneToOneField('Release')
   features = models.ManyToManyField('Feature', blank=True, null=True)
   feedback = models.CharField(max_length=1028)

class Customer(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200) 
   organization = models.CharField(max_length=200, blank=True, null=True)
   #location = 

class Release(models.Model):
   release_date = models.DateTimeField()
   pass_fail_criteria = models.CharField(max_length=1028, blank=True, null=True)
   market = models.CharField(max_length=200, blank=True, null=True) #maybe define class for market
   #documents
   #marketing_documents
   #press_release_documents
   roadmap = models.ForeignKey('Roadmap', blank=True, null=True)

class Risk(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=200)
   category = models.ManyToManyField('Category', blank=True, null=True)
   release = models.ForeignKey('Release', blank=True, null=True)
   features = models.ManyToManyField('Feature', blank=True, null=True)
   probability = models.CharField(max_length=128, choices=PROBABILITY_CHOICES)
   severity = models.CharField(max_length=128, choices=PRIORITY_CHOICES)
   status = models.CharField(max_length=128, choices=RISK_CHOICES)

class Team(models.Model):
   #manager = models.ForeignKey('Member')
   name = models.CharField(max_length=200)

class Member(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   title = models.CharField(max_length=200, blank=True, null=True)
   team = models.ForeignKey('Team')
   is_manager = models.BooleanField(default=False)
   #photo
   #permissions

class Milestone(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=200)
   category = models.ManyToManyField('Category', blank=True, null=True)
   #phase
   start_date = models.DateTimeField(default=datetime.now)
   end_date = models.DateTimeField()
   release = models.ForeignKey('Release')
   successors = models.ManyToManyField('Milestone', blank=True, null=True)
   percent_complete = models.IntegerField()
   roadmap = models.ForeignKey('Roadmap', blank=True, null=True)

class Roadmap(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=200)
   category = models.ManyToManyField('Category', blank=True, null=True)
   end_date = models.DateTimeField(blank=True)
   features = models.ManyToManyField('Feature', blank=True, null=True)
   market = models.CharField(max_length=200, blank=True, null=True) #maybe define class for market
   customers  = models.ManyToManyField('Customer', blank=True, null=True)
