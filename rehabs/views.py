from django.shortcuts import render
from .models import RehabilitationCenter
# Create your views here.

def find_help(request):
    centers = RehabilitationCenter.objects.all()
    return render(request, 'rehabs/find_help.html', {'centers': centers})