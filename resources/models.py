from django.db import models

# Create your models here.

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('individual', 'For Individuals'),
        ('family', 'For Families and Caregivers'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
