from django.urls import path
from . import views

urlpatterns = [
    path('attactions/', views.attraction_details, name='attractions'),
]