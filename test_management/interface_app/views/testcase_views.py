from django.shortcuts import render

# Create your views here.
def testcase(request):
    return render(request, "testcase_manage.html")