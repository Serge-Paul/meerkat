from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_risks(request):
   risk_list = Risk.objects.all().order_by('-id')
   return render_to_response('risks/view_all_risks.html', {'risk_list': risk_list})


def create_risk(request):
   return HttpResponse("You're adding new risk")

def view_risk(request, risk_id):
   return HttpResponse("You're looking at risk %s." % risk_id)

def edit_risk(request, risk_id):
   return HttpResponse("You're editing risk %s." % risk_id)

