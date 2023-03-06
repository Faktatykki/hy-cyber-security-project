from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Secret

@login_required
def homePageView(request):
    all = User.objects.all()

    print(all, "haloo")
    return render(request, 'index.html')

def somethingView(request):
    return HttpResponse("What?")