from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_risks(request):
   risk_list = Risk.objects.all().order_by('-id')
   return render_to_response('risks/view_all_risks.html', {'risk_list': risk_list})

def create_risk(request):
   return HttpResponse("You're adding new risk")

def view_risk(request, risk_id):
   risk = Risk.objects.get(id = risk_id)
   component = Component.objects.filter(risk = risk_id)
   bug = Bug.objects.filter(risk = risk_id)
   feature = Feature.objects.filter(risk = risk_id)

   return render_to_response('risks/view_risk.html', {'risk': risk, 'bug': bug, 'component': component, 'feature': feature})

def edit_risk(request, risk_id):
   return HttpResponse("You're editing risk %s." % risk_id)

def delete_risk(request, risk_id):

   risk = Risk.objects.get(id = risk_id)
   risk.delete()

   return redirect('apps.devproc.views.risk.view_all_risks')   

