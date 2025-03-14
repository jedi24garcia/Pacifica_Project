from django.shortcuts import render

# Create your views here.
def base(request):
  return render(request, 'homepage.html')

def AboutPage(request):
  return render(request, 'aboutpage.html')

def WorkWithUsPage(request):
  return render(request, 'workpage.html')

def MediaPage(request):
  return render(request, 'mediapage.html')

def ResourcesPage(request):
  return render(request, 'resourcespage.html')