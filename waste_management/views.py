# waste_management/views.py
from django.shortcuts import render

def home(request):
    """Home page view that serves as the default route"""
    return render(request, 'home.html')