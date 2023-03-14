from django.urls import path

from .views import homePageView, somethingView, addView, registerView, secretsView

urlpatterns = [
    path('', homePageView, name='home'),
    #path('secrets/', secretsView, name='secrets'),
    path('secrets/<str:user>/', secretsView, name='secrets'),
    path('something/', somethingView, name='something'),
    path('add/', addView, name='add'),
    path('register/', registerView, name='register'),
]