from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Handles requests to the home page."""
    return HttpResponse("Hello, world. You're at the home index.")
