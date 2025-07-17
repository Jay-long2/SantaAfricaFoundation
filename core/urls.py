from django.urls import path
from . import views
from programs import views as program_views
from resources import views as resource_list_views
from rehabs import views as rehab_views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/',resource_list_views.resource_list, name='resources'),
    path('programs/', program_views.program_list, name='programs'),
    path('contact/', views.contact, name='contact'),
    path('contact-details/', views.contact_details, name='contact_details'),
    path('terms/', views.terms, name='terms'),
    path('privacy/',views.privacy, name='privacy'),
    path('find-help/', rehab_views.find_help, name='find_help'),
]
