from django.http import HttpResponse


def view_all_risks(request):
   return HttpResponse("Hello, world. You're viewing all risks")

def create_risk(request):
   return HttpResponse("You're adding new risk")

def view_risk(request, risk_id):
   return HttpResponse("You're looking at risk %s." % risk_id)

def edit_risk(request, risk_id):
   return HttpResponse("You're editing risk %s." % risk_id)

