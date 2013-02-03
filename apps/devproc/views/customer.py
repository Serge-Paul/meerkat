from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required

class CustomerForm(forms.Form):
   first_name = forms.CharField(max_length=200)
   last_name = forms.CharField(max_length=200)
   organization = forms.CharField(max_length=200)
   location = forms.CharField(max_length=200, required=False)


@login_required
def view_all_customers(request):
   return HttpResponse("Hello, world. You're viewing all customers")


@login_required
def create_customer(request):
   if request.method == 'POST':

      form = CustomerForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         customer = Customer()
         customer.first_name = form.cleaned_data['first_name']
         customer.last_name = form.cleaned_data['last_name']
	 customer.organization = form.cleaned_data['organization'] 
	 customer.location = form.cleaned_data['location']	

         customer.save()

         return redirect('apps.devproc.views.customer.view_customer', customer_id = customer.id)

      else: #if form is not valid
         return render_to_response('customers/create_customer.html', {'user' : request.user, 'form':form, 'message': 'Error adding customer. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = CustomerForm()
      return render_to_response('customers/create_customer.html', {'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_customer(request, customer_id):
  customer = Customer.objects.get(id = customer_id)
  return render_to_response('customers/view_customer.html', {'user' : request.user, 'customer': customer})


@login_required
def edit_customer(request, customer_id):

   customer = Customer.objects.get(id = customer_id)

   if request.method == 'POST':

      form = CustomerForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         customer.first_name = form.cleaned_data['first_name']
         customer.last_name = form.cleaned_data['last_name']
         customer.organization = form.cleaned_data['organization']
         customer.location = form.cleaned_data['location']

         customer.save()

         return redirect('apps.devproc.views.customer.view_customer', customer_id = customer.id)

      else: #if form is not valid
         return render_to_response('customers/create_customer.html', {'user' : request.user, 'form':form, 'message': 'Error editing customer. Please try again.', 'customer': customer, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
     
      defaults = {
                 'first_name' : customer.first_name,
                 'last_name' : customer.last_name,
                 'organization' : customer.organization,
                 'location' : customer.location,
                 }

      form = CustomerForm(initial=defaults)

      return render_to_response('customers/create_customer.html', {'user' : request.user, 'form': form, 'customer': customer, 'mode': 'edit'},  context_instance=RequestContext(request))



@login_required
def delete_customer(request, customer_id):

   customer = Customer.objects.get(id = customer_id)
   customer.delete()

   return redirect('apps.devproc.views.customer.view_all_customers')   
                                                              
