from django.urls import path
from . import views

urlpatterns = [
    path('', views.dine, name='dine'),
]