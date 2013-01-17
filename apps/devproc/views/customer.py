from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_customers(request):
   return HttpResponse("Hello, world. You're viewing all customers")

def create_customer(request):
   return HttpResponse("You're adding new customer")

def view_customer(request, customer_id):
  customer = Customer.objects.get(id = customer_id)
  return render_to_response('customers/view_customer.html', {'customer': customer})


def edit_customer(request, customer_id):
   return HttpResponse("You're editing customer %s." % customer_id)
                                                              
