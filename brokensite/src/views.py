from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Secret

@login_required
def homePageView(request):
    username = None

    if request.user.is_authenticated:
        username = request.user.username

    return render(request, 'index.html', { "username": username })

def somethingView(request):
    return HttpResponse("What?")