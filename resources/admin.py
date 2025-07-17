from django.contrib import admin
from .models import Resource
# Register your models here.
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
