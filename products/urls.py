from django.urls import path
from . import views
from .views import PurchaseView

urlpatterns = [
    path('store/', views.store_details, name='store'),
    path('purchase/<int:pk>', PurchaseView.as_view(), name='buy_products'),
]