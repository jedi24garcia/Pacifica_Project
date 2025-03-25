from django.db import models

# Create your models here.
class Attraction(models.Model):
# first part
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.TextField(max_length=100, default="No features available")
    image = models.ImageField(upload_to='dine_images/', null=True, blank=True)

# second part
    activity_name = models.CharField(max_length=100, null=True, blank=True)
    activity_description = models.TextField(null=True, blank=True)
    activity_image = models.ImageField(upload_to='dine_images/', null=True, blank=True)
    activity_name_2 = models.CharField(max_length=100, null=True, blank=True)
    activity_description_2 = models.TextField(null=True, blank=True)
    activity_image_2 = models.ImageField(upload_to='dine_images/', null=True, blank=True)

    def __str__(self):
        return self.name