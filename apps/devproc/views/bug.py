from django.http import HttpResponse


def view_all_bugs(request):
   return HttpResponse("Hello, world. You're viewing all bugs")

def create_bug(request):
   return HttpResponse("You're adding new bug")

def view_bug(request, bug_id):
   return HttpResponse("You're looking at bug %s." % bug_id)

def edit_bug(request, bug_id):
   return HttpResponse("You're editing bug %s." % bug_id)                                                           
