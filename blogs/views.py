from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.
def blog_details(request):
    if request.method == "POST":
        content = request.POST.get("blog_content")
        image = request.FILES.get("image")
        if content:
            Blog.objects.create(user=request.user, content=content, image=image)
            return redirect("blog_details")
    
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_details.html', {'blogs': blogs})