from django.urls import path

from .views import homePageView, somethingView, addView, registerView

urlpatterns = [
    path('', homePageView, name='home'),
    path('something/', somethingView, name='something'),
    path('add/', addView, name='add'),
    path('signup/', registerView, name='register'),
]