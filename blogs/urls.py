from django.urls import path
from . import views
from .views import blog_details

urlpatterns = [
    path('blogs/', blog_details, name='blog_details')
]