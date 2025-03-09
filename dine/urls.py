from django.urls import path
from . import views
from .views import DineDetailView

urlpatterns = [
    # path('', views.dine_details, name='dine_list'), # Don't worry for now
    path('dines/<int:pk>/', DineDetailView.as_view(), name='dine_details'),
]