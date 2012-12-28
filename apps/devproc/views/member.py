from django.http import HttpResponse


def view_all_members(request):
   return HttpResponse("Hello, world. You're viewing all members")

def create_member(request):
   return HttpResponse("You're adding new member")

def view_member(request, member_id):
   return HttpResponse("You're looking at member %s." % member_id)

def edit_member(request, member_id):
   return HttpResponse("You're editing member %s." % member_id)                                                              
