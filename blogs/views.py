from django.shortcuts import render

# Create your views here.
def UserBlogs(request):
    return render(request, 'blog_details.html')