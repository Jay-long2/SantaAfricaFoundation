from django.shortcuts import render
from .models import Program
from django.http import HttpResponse
# Create your views here.

def program_list(request):
    programs = Program.objects.all().order_by('-created_at')
    return render(request,'programs/program_list.html', {'programs': programs})

