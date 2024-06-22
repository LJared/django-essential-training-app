from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    """Handles requests to the home page."""
    return render(request, "home/welcome.html", {
        'today': datetime.today(),
    })
