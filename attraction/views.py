from django.shortcuts import render
from django.views.generic import DetailView
from .models import Attraction

# Create your views here.
def attraction_details(request):
    return render(request, 'attractions_details.html')

class AttractionsDetailView(DetailView):
    model = Attraction
    template_name = "attractions_details.html"