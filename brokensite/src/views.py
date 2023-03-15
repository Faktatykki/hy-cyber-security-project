from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db import connection

from .models import Secret


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit = False)

            username = form.data.get("username")
            raw_password = form.data.get("password1")
            
            user.username = username
            user.set_password(raw_password)
            user.save()

            return redirect("home")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})

#@login_required
#def secretsView(request, user):
#    logged_user = None
#    user = User.objects.filter(username=user)[0]
#
#    if user == request.user:
#        logged_user = user
#        secrets = Secret.objects.filter(owner=logged_user)
#    else:
#        return render(request, "index.html", { "user": request.user.username })
#
#    return render(request, "secrets.html", { "secrets" : secrets, "user" : logged_user.username})

def secretsView(request, user):
    user = User.objects.filter(username=user)
    secrets = Secret.objects.filter(owner=user[0].id)
    
    return render(request, 'secrets.html', { "secrets": secrets , "user": user })

@login_required
def homePageView(request):
    logged_user = None

    if request.user.is_authenticated:
        logged_user= request.user
        
    return render(request, 'index.html', { "username": logged_user.username })

#@login_required
#def addView(request):
#    logged_user = request.user
#
#    if request.method == "POST":
#        input_secret = request.POST.get("secret")
#
#        Secret.objects.create(owner=logged_user, content=input_secret)
#
#    return redirect('/')

@login_required
def addView(request):
    logged_user = request.user.id

    if request.method == "POST":
        input_secret = request.POST.get("secret")

        with connection.cursor() as cursor:
            cursor.executescript("INSERT INTO secrets (content, owner_id) VALUES (" + input_secret + ", " + str(logged_user) +")")

    return redirect('/')