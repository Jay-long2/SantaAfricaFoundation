from django.db import models

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='program_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
