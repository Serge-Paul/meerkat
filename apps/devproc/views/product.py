from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *


class ProductForm(forms.Form):
   name = forms.CharField(max_length=250) 
   description= forms.CharField(max_length=1028, widget=forms.Textarea, required=False)


@login_required
def view_all_products(request):
   session_info = get_session_info(request)

   product_list = Product.objects.all().order_by('-id')
   return render_to_response('products/view_all_products.html', {'session_info': session_info, 'user' : request.user, 'product_list': product_list})


@login_required
def create_product(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = ProductForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         product = Product()
         product.name = form.cleaned_data['name']
         product.description = form.cleaned_data['description']
           
         product.company = request.user.profile.company
     
         product.save()
 
         return redirect('apps.devproc.views.product.view_product', product_id = product.id)
    
      else: #if form is not valid
          return render_to_response('products/create_product.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating product. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = ProductForm()
      return render_to_response('products/create_product.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_product(request, product_id):

   product = Product.objects.get(id = product_id)

   #change the session variable
   request.session['active_product'] = product.id
   request.session.save()

   session_info = get_session_info(request)

   return render_to_response('products/view_product.html', {'session_info': session_info, 'user' : request.user, 'product': product })


@login_required
def edit_product(request, product_id):
   session_info = get_session_info(request)
   
   product = Product.objects.get(id = product_id)

   if request.method == 'POST':
  
      form = ProductForm(request.POST)
  
      # Do when form is submitted
      if form.is_valid():

         product.name = form.cleaned_data['name']
         product.description = form.cleaned_data['description']
         product.save()

         return redirect('apps.devproc.views.product.view_product', product_id = product.id)
    
      else: #if form is not valid 
          return render_to_response('products/create_product.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing product. Please try again.', 'product': product, 'mode': 'edit'}, context_instance=RequestContext(request))

   else: #code for just initially displaying form
      
      defaults = { 
                 'name' : product.name, 
                 'description': product.description,
                 }

      form = ProductForm(initial=defaults)   
 
      return render_to_response('products/create_product.html', {'session_info': session_info, 'user' : request.user, 'form': form, 'product': product, 'mode': 'edit' },  context_instance=RequestContext(request))


@login_required
def delete_product(request, product_id):
   session_info = get_session_info(request)
   
   product = Product.objects.get(id = product_id)
   product.delete()

   #change the session variable
   if Product.objects.filter(company = request.user.profile.company.id).count() != 0: 
      active_product = Product.objects.filter(company = request.user.profile.company.id)[0]

      request.session['active_product'] = active_product.id
      request.session.save()

   return redirect('apps.devproc.views.product.view_all_products')   


