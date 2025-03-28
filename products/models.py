from django.db import models

# Create your models here.
class Purchase(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    description_one = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='dine_images/', null=True, blank=True)

    def __str__(self):
        return self.name