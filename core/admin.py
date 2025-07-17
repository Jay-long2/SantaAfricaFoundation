from django.contrib import admin
from .models import NewsletterSubscriber
from .models import ContactMessage

# Register your models here.
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    ordering = ('-subscribed_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('sent_at',)
    ordering = ('-sent_at',)


