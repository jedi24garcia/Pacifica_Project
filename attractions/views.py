from django.shortcuts import render

# Create your views here.
def attraction_details(request):
    return render(request, 'attractions_details.html')