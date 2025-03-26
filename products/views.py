from django.shortcuts import render

# Create your views here.
def store_details(request):
    return render(request, 'product_details.html')