from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_features(request):
   feature_list = Feature.objects.all().order_by('-id')
   return render_to_response('features/view_all_features.html', {'feature_list': feature_list})



def create_feature(request):
   return HttpResponse("You're adding new feature")

def view_feature(request, feature_id):
   feature = Feature.objects.get(id = feature_id)
   return render_to_response('features/view_feature.html', {'feature': feature})


def edit_feature(request, feature_id):
   return HttpResponse("You're editing feature %s." % feature_id)


def delete_feature(request, feature_id):

   feature = Feature.objects.get(id = feature_id)
   feature.delete()

   return redirect('apps.devproc.views.feature.view_all_features')   
                                                              
