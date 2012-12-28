from django.http import HttpResponse


def view_all_features(request):
   return HttpResponse("Hello, world. You're viewing all features")

def create_feature(request):
   return HttpResponse("You're adding new feature")

def view_feature(request, feature_id):
   return HttpResponse("You're looking at feature %s." % feature_id)

def edit_feature(request, feature_id):
   return HttpResponse("You're editing feature %s." % feature_id)
                                                              
