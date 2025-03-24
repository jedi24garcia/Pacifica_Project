from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # link the user who wrote the blog
    content = models.TextField()
    image = models.ImageField(upload_to='dine_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # timestamp for when the post was created

    def __str__(self):
        return f"Blog by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"