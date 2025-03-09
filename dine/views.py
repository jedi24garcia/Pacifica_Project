from django.shortcuts import render

# Create your views here.
def dine_details(request):
    return render(request, 'dine_details.html')