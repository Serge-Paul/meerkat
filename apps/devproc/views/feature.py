from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_features(request):
   feature_list = Feature.objects.all().order_by('-id')
   return render_to_response('features/view_all_features.html', {'feature_list': feature_list})



def create_feature(request):
   return HttpResponse("You're adding new feature")

def view_feature(request, feature_id):
   return HttpResponse("You're looking at feature %s." % feature_id)

def edit_feature(request, feature_id):
   return HttpResponse("You're editing feature %s." % feature_id)
                                                              
