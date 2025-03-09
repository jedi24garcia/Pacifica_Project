from django.shortcuts import render
from django.views.generic import DetailView
from .models import Dine

# Create your views here.
def dine_details(request):
    return render(request, 'dine_details.html')

class DineDetailView(DetailView):
    model = Dine
    template_name = "dine_details.html"