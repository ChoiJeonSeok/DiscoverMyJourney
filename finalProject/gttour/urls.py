from django.urls import path

from . import views

app_name = 'gttour'

urlpatterns = [
    path('', views.index, name='index'),
]