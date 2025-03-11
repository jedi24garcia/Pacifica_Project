from django.db import models

# Create your models here.
class Dine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.TextField(max_length=100, default="No features available")
    image = models.ImageField(upload_to='dine_images/', null=True, blank=True)

    def __str__(self):
        return self.name