from django.urls import path

from .views import homePageView, somethingView

urlpatterns = [
    path('', homePageView, name='home'),
    path('something/', somethingView, name='something')
]