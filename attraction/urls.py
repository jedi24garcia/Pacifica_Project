from django.urls import path
from . import views
from .views import AttractionsDetailView

urlpatterns = [
    path('attractions/<int:pk>/', AttractionsDetailView.as_view(), name='attraction_details'),
]