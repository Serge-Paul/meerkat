from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.devproc.models import *


def view_all_tests(request):
   test_list = Test.objects.all().order_by('-id')
   return render_to_response('tests/view_all_tests.html', {'test_list': test_list})

def create_test(request):
   return HttpResponse("You're adding new test")

def view_test(request, test_id):
   test = Test.objects.get(id = test_id)
   bugs = Bug.objects.filter(test = test_id)
   return render_to_response('tests/view_test.html', {'test': test, 'bugs': bugs})

def edit_test(request, test_id):
   return HttpResponse("You're editing test %s." % test_id)

def delete_test(request, test_id):

   test = Test.objects.get(id = test_id)
   test.delete()

   return redirect('apps.devproc.views.test.view_all_tests')   

