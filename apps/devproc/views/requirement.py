from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from apps.devproc.models import *
from django import forms
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.devproc.utils import *
from multiuploader.forms import MultiUploadForm
from multiuploader.forms import MultiuploaderField

class RequirementForm(forms.Form):
   title = forms.CharField(max_length=200)
   description = forms.CharField(max_length=1028, widget=forms.Textarea)
   category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False) 
   parent = forms.ModelChoiceField(queryset=Requirement.objects.all(), required=False) #need to prevent chosing current reqmt as parent
   use_case = forms.ModelChoiceField(queryset=UseCase.objects.all(), required=False, label="Supporting Use Case")
   priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
   release = forms.ModelChoiceField(queryset=Release.objects.all(), required=False)
   approval_status = forms.ChoiceField(choices=APPROVAL_STATUS_CHOICES)
   identifier = forms.CharField(max_length=200)
   source = forms.ChoiceField(choices=SOURCE_CHOICES)
   notes = forms.CharField(max_length=1028, widget=forms.Textarea, required=False)  
   responsible_engineer = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), label="Product Manager or Engineer", required=False)
   #uploadedFiles = MultiuploaderField(required=False)
   file1 = forms.CharField(max_length=200, widget=forms.HiddenInput(), required=False)
   file1_url = forms.CharField(max_length=200, widget=forms.HiddenInput(), required=False)
   file1_delete_url = forms.CharField(max_length=200, widget=forms.HiddenInput(), required=False)

@login_required
def view_all_reqmts(request): 
   session_info = get_session_info(request)

   reqmt_list = Requirement.objects.filter(product = session_info['active_product']).order_by('-id')

   return render_to_response('requirements/view_all_reqmts.html', {'session_info': session_info, 'user' : request.user, 'reqmt_list': reqmt_list})


@login_required
def create_reqmt(request):
   session_info = get_session_info(request)

   if request.method == 'POST':

      form = RequirementForm(request.POST, request.FILES)
      uploadForm = MultiUploadForm(request.POST, request.FILES)

      #print dir(uploadForm.files.items)


      # Do when form is submitted
      if form.is_valid():

         #print form.cleaned_data['uploadedFiles']
         #print request.FILES['uploadedFiles']
 
         reqmt = Requirement()
         reqmt.title = form.cleaned_data['title']
         reqmt.description = form.cleaned_data['description']
	 reqmt.parent = form.cleaned_data['parent']
	 reqmt.use_case = form.cleaned_data['use_case']
	 reqmt.priority = form.cleaned_data['priority']
	 reqmt.release = form.cleaned_data['release']
	 reqmt.approval_status = form.cleaned_data['approval_status']
	 reqmt.identifier = form.cleaned_data['identifier']
	 reqmt.source = form.cleaned_data['source']
	 reqmt.notes = form.cleaned_data['notes']
         reqmt.product= session_info['active_product']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         reqmt.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            reqmt.category = form.cleaned_data['category'].all() # ManyToMany
        
         if form.cleaned_data['responsible_engineer']: 
            reqmt.responsible_engineer = form.cleaned_data['responsible_engineer'].all() 

         reqmt.save()

         return redirect('apps.devproc.views.requirement.view_reqmt', reqmt_id = reqmt.id)

      else: #if form is not valid
         return render_to_response('requirements/create_reqmt.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error creating requirement. Please try again.', 'mode': 'create'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
      form = RequirementForm()
      uploadForm = MultiUploadForm()

      return render_to_response('requirements/create_reqmt.html', {'upload_form': uploadForm, 'session_info': session_info, 'user' : request.user, 'form': form, 'mode': 'create'},  context_instance=RequestContext(request))


@login_required
def view_reqmt(request, reqmt_id):
   session_info = get_session_info(request)

   #get all files attached to this requirement
   attachments = FileAttachment.objects.filter(requirement = reqmt_id)

   reqmt = Requirement.objects.get(id = reqmt_id)
   return render_to_response('requirements/view_reqmt.html', {'session_info': session_info, 'user' : request.user, 'reqmt': reqmt, 'attachments': attachments})


@login_required
def edit_reqmt(request, reqmt_id):
   session_info = get_session_info(request)

   reqmt = Requirement.objects.get(id = reqmt_id)

   if request.method == 'POST':

      form = RequirementForm(request.POST)

      # Do when form is submitted
      if form.is_valid():

         reqmt.title = form.cleaned_data['title']
         reqmt.description = form.cleaned_data['description']
         reqmt.parent = form.cleaned_data['parent']
         reqmt.use_case = form.cleaned_data['use_case']
         reqmt.priority = form.cleaned_data['priority']
         reqmt.release = form.cleaned_data['release']
         reqmt.approval_status = form.cleaned_data['approval_status']
         reqmt.identifier = form.cleaned_data['identifier']
         reqmt.source = form.cleaned_data['source']
         reqmt.notes = form.cleaned_data['notes']

# Have to save because instance needs to have a primary key value before a many-to-many relationship can be used.
         reqmt.save()

         if form.cleaned_data['category']: #This field is optional, so need if stmt just in case item is not selected
            reqmt.category = form.cleaned_data['category'].all() # ManyToMany

         if form.cleaned_data['responsible_engineer']: 
            reqmt.responsible_engineer = form.cleaned_data['responsible_engineer'].all()

         reqmt.save()

         if form.cleaned_data['file1']:
	    file1 = FileAttachment()
             #UPDATING THE FILE NAME IS NOT WORKING. WHEN DISPLAY FILE THE NAME IS THE SAME AS THE PATH
             #cant' change file.path because it's read only, so setting file = url instead of file.path = url
            #file1.file.name = form.cleaned_data['file1']
            file1.file = form.cleaned_data['file1_url']
            file1.company = request.user.profile.company 
            file1.filename = form.cleaned_data['file1']
            #file1.url = form.cleaned_data['file1_url'] 
            #file1.delete_url = form.cleaned_data['file1_delete_url']
            file1.requirement = reqmt
            file1.save()
        
         return redirect('apps.devproc.views.requirement.view_reqmt', reqmt_id = reqmt.id)

      else: #if form is not valid
         return render_to_response('requirements/create_reqmt.html', {'session_info': session_info, 'user' : request.user, 'form':form, 'message': 'Error editing requirement. Please try again.', 'reqmt': reqmt, 'mode': 'edit'}, context_instance=RequestContext(request))


   else: #code for just initially displaying form
  
      defaults = {
                 'title' : reqmt.title,
                 'description' : reqmt.description,
                 'parent' : reqmt.parent,
                 'use_case' : reqmt.use_case,
                 'priority' : reqmt.priority,
                 'release' : reqmt.release,
                 'approval_status' : reqmt.approval_status,
                 'identifier' : reqmt.identifier,
                 'source' : reqmt.source,
                 'notes' : reqmt.notes,
                 'category' : reqmt.category.all(),
                 'responsible_engineer': reqmt.responsible_engineer.all()
                 }

      form = RequirementForm(initial=defaults)

      #get all files attached to this requirement
      attachments = FileAttachment.objects.filter(requirement = reqmt_id)

      return render_to_response('requirements/create_reqmt.html', {'attachments': attachments, 'session_info': session_info, 'user' : request.user, 'form': form, 'reqmt': reqmt, 'mode': 'edit'},  context_instance=RequestContext(request))



@login_required
def delete_reqmt(request, reqmt_id):
   session_info = get_session_info(request)

   reqmt = Requirement.objects.get(id = reqmt_id)
   reqmt.delete()

   return redirect('apps.devproc.views.requirement.view_all_reqmts')   

