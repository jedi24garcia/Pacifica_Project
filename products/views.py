from django.shortcuts import render
from django.views.generic import DetailView
from .models import Purchase

# Create your views here.
def store_details(request):
    return render(request, 'product_details.html')

# def purchase(request):
#     return render(request, 'buy_product.html')

class PurchaseView(DetailView):
    model = Purchase
    template_name = "buy_product.html"