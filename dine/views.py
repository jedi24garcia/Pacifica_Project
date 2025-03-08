from django.shortcuts import render

# Create your views here.
def dine(request):
    return render(request, 'dine_details.html')