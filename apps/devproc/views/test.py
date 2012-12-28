from django.http import HttpResponse


def view_all_tests(request):
   return HttpResponse("Hello, world. You're viewing all tests")

def create_test(request):
   return HttpResponse("You're adding new test")

def view_test(request, test_id):
   return HttpResponse("You're looking at test %s." % test_id)

def edit_test(request, test_id):
   return HttpResponse("You're editing test %s." % test_id)

