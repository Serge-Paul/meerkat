from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required

class FeatureForm(forms.Form):
   title = forms.CharField(max_length=200)
   design_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   implementation_description = forms.CharField(max_length=1028, widget=forms.Textarea) 
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   responsible_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False) 
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=True) 
   approval_status = forms.ChoiceField(choices=APPROVAL_STATUS_CHOICES)
   usecases = forms.ModelMultipleChoiceField(queryset=UseCase.objects.all(), required=False) 
   requirements = forms.ModelMultipleChoiceField(queryset=Requirement.objects.all(), required=False) 
   identifier = forms.CharField(max_length=200)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False) 
   component = forms.ModelMultipleChoiceField(queryset=Component.objects.all(), required=False) 


@login_required
def view_all_features(request):
   feature_list = Feature.objects.all().order_by('-id')
   return render_to_response('features/view_all_features.html', {'user' : request.user, 'feature_list': feature_list})



@login_required
def create_feature(request):
   if request.method == 'POST':

      form = FeatureForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         feature = Feature()
         feature.title = form.cleaned_data['title']
         feature.design_description = form.cleaned_data['design_description']
	 feature.implementation_description = form.cleaned_data['implementation_description']
	 feature.release = form.cleaned_data['release']
	 feature.approval_status = form.cleaned_data['approval_status']
	 feature.identifier = form.cleaned_data['identifier']
	 feature.notes = form.cleaned_data['notes']


# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         feature.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            feature.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['responsible_engineer']:
	    feature.responsible_engineer = form.cleaned_data['responsible_engineer'].all()        

         if form.cleaned_data['usecases']:
	    feature.usecases = form.cleaned_data['usecases'].all()

         if form.cleaned_data['requirements']:
	    feature.requirements = form.cleaned_data['requirements'].all()

         if form.cleaned_data['component']:
	    feature.component = form.cleaned_data['component'].all()

         feature.save()

         return redirect('apps.devproc.views.feature.view_feature', feature_id = feature.id)

      else: #if form is not valid
         return render_to_response('features/create_feature.html', {'user' : request.user, 'form':form, 'message': 'Error creating feature. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = FeatureForm()
      return render_to_response('features/create_feature.html', {'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_feature(request, feature_id):
   feature = Feature.objects.get(id = feature_id)
   risks = Risk.objects.filter(feature = feature)

   return render_to_response('features/view_feature.html', {'user' : request.user, 'feature': feature, 'risks': risks})


@login_required
def edit_feature(request, feature_id):

   feature = Feature.objects.get(id = feature_id)

   if request.method == 'POST':

      form = FeatureForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         feature.title = form.cleaned_data['title']
         feature.design_description = form.cleaned_data['design_description']
         feature.implementation_description = form.cleaned_data['implementation_description']
         feature.release = form.cleaned_data['release']
         feature.approval_status = form.cleaned_data['approval_status']
         feature.identifier = form.cleaned_data['identifier']
         feature.notes = form.cleaned_data['notes']


# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         feature.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            feature.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['responsible_engineer']:
            feature.responsible_engineer = form.cleaned_data['responsible_engineer'].all()

         if form.cleaned_data['usecases']:
            feature.usecases = form.cleaned_data['usecases'].all()

         if form.cleaned_data['requirements']:
            feature.requirements = form.cleaned_data['requirements'].all()

         if form.cleaned_data['component']:
            feature.component = form.cleaned_data['component'].all()

         feature.save()

         return redirect('apps.devproc.views.feature.view_feature', feature_id = feature.id)

      else: #if form is not valid
         return render_to_response('features/create_feature.html', {'user' : request.user, 'form':form, 'message': 'Error creating feature. Please try again.', 'feature': feature, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      
      defaults = {
                 'title' : feature.title,
                 'design_description': feature.design_description,
                 'implementation_description' : feature.implementation_description,
                 'release' : feature.release,
                 'approval_status' : feature.approval_status,
                 'identifier' : feature.identifier,
                 'notes' : feature.notes,
                 'category' : feature.category.all(),
                 'responsible_engineer' : feature.responsible_engineer.all(),
                 'usecases' : feature.usecases.all(),
                 'requirements' : feature.requirements.all(),
                 'component' : feature.component.all(),
                 }

      form = FeatureForm(initial=defaults)

      return render_to_response('features/create_feature.html', {'user' : request.user, 'form': form, 'feature': feature, 'mode': 'edit'},  context_instance=RequestContext(request))


@login_required
def delete_feature(request, feature_id):

   feature = Feature.objects.get(id = feature_id)
   feature.delete()

   return redirect('apps.devproc.views.feature.view_all_features')   
                                                              
