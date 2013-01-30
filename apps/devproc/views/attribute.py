from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext

class AttributeForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028)
  

def view_all_attributes(request, component_id):

#View all attributes associated with a specific component

   component = Component.objects.get(id = component_id)
   attribute_list = Attribute.objects.filter(component = component)

   return render_to_response('attributes/view_all_attributes.html', {'attribute_list': attribute_list, 'component': component})
 

def create_attribute(request, component_id):

   component = Component.objects.get(id = component_id)

   if request.method == 'POST':

      form = AttributeForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         attribute = Attribute()
         attribute.title = form.cleaned_data['title']
         attribute.description = form.cleaned_data['description']            

         attribute.component = component
 
         attribute.save()
      
         return redirect('apps.devproc.views.attribute.view_attribute', component_id = component.id, attribute_id = attribute.id)

      else: #if form is not valid
         return render_to_response('attributes/create_attribute.html', {'form':form, 'message': 'Error creating attribute. Please try again.', 'component': component}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = AttributeForm()
      return render_to_response('attributes/create_attribute.html', {'form': form, 'component': component},  context_instance=RequestContext(request))


def view_attribute(request, component_id, attribute_id):
   attribute = Attribute.objects.get(id = attribute_id)
   component = Component.objects.get(id = component_id)
   return render_to_response('attributes/view_attribute.html', {'attribute': attribute, 'component': component})


def edit_attribute(request, attribute_id):
   return HttpResponse("You're editing attribute %s." % attribute_id)

def delete_attribute(request, attribute_id):

   attribute = Attribute.objects.get(id = attribute_id)
   
   component = attribute.component 

   attribute.delete()

   return redirect('apps.devproc.views.attribute.view_all_attributes', component_id = component.id)   



