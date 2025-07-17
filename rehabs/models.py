from django.db import models

# Create your models here.
class RehabilitationCenter(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField()
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='rehab_centers/', blank=True)

    def __str__(self):
        return self.name