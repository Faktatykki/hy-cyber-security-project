from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Secret

@login_required
def homePageView(request):
    logged_user = None
    secrets = None

    if request.user.is_authenticated:
        logged_user= request.user
        secrets = Secret.objects.filter(owner=logged_user)


    return render(request, 'index.html', { "username": logged_user.username, "secrets" : secrets })

@login_required
def addView(request):
    logged_user = request.user

    if request.method == "POST":
        input_secret = request.POST.get("secret")
        print(input_secret)
        Secret.objects.create(owner=logged_user, content=input_secret)

    return redirect('/')

def somethingView(request):
    return HttpResponse("What?")