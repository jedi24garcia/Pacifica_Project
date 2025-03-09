from django.urls import path
from . import views

urlpatterns = [
    path('', views.dine_details, name='dine_details'),
]