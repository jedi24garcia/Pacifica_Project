from django.db import models

# Create your models here.
class Dine(models.Model):
# first part
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.TextField(max_length=100, default="No features available")
    image = models.ImageField(upload_to='dine_images/', null=True, blank=True)

# second part 
    name_1 = models.CharField(max_length=100, null=True, blank=True)
    description_1 = models.TextField(null=True, blank=True)
    features_1 = models.TextField(max_length=100, default="No features available")
    image_1 = models.ImageField(upload_to='dine_images/', null=True, blank=True)

# third part
    name_2 = models.CharField(max_length=100, null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    features_2 = models.TextField(max_length=100, default="No features available")
    image_2 = models.ImageField(upload_to='dine_images/', null=True, blank=True)

    def __str__(self):
        return self.name