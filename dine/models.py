from django.db import models

# Create your models here.
class Dine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.TextField(max_length=100, default="No features available")

    def __str__(self):
        return self.name