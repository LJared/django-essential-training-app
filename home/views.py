from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

def home(request):
    """Handles requests to the home page."""
    return render(request, "home/welcome.html", {
        'today': datetime.today(),
    })


@login_required(login_url='/admin')
def authorized(request):
    """Handles requests to the authorized page."""
    return render(request, "home/authorized.html", {})