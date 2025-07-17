from django.shortcuts import render
from .models import Resource
# Create your views here.


def resource_list(request):
    individual_resources = Resource.objects.filter(category='individual')
    family_resources = Resource.objects.filter(category='family')
    return render(request, 'resources/resource_list.html', {
        'individual_resources': individual_resources,
        'family_resources': family_resources
    })
