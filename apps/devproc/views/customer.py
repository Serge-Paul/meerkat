from django.http import HttpResponse


def view_all_customers(request):
   return HttpResponse("Hello, world. You're viewing all customers")

def create_customer(request):
   return HttpResponse("You're adding new customer")

def view_customer(request, customer_id):
   return HttpResponse("You're looking at customer %s." % customer_id)

def edit_customer(request, customer_id):
   return HttpResponse("You're editing customer %s." % customer_id)
                                                              
