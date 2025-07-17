from django.contrib import admin
from .models import RehabilitationCenter
# Register your models here.
@admin.register(RehabilitationCenter)
class RehabilitationCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone_number')
    search_fields = ('name', 'location')
