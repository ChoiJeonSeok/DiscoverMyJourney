from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'gttour/gttour.html')