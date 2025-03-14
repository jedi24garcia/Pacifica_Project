from django.urls import path
from . import views

urlpatterns = [
  path('', views.base, name='homepage'),
  path('about/', views.AboutPage, name='about'),
  path('work/', views.WorkWithUsPage, name='work'),
  path('media/', views.MediaPage, name='media'),
  path('resources/', views.ResourcesPage, name='resources'),
]