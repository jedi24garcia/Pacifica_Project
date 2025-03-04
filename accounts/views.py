from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, SignUpForm, ProfileForm
from .models import Profile

# Create your views here.

# Define login page
def UserLogin(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('base') # redirect to home after login
      else:
         messages.error(request, "Invalid username or password")  
    else:
      messages.error(request, "Form is not valid")
  else:
      form = LoginForm()
  return render(request, 'login.html', {'form': form})

# Define signup page
def UserSignUp(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save() 
      login(request, user)
      messages.success(request, "Signup successful! Please login.")
      return redirect('base') # redirect to hom after signup
    else:
      print("Form is not valid:", form.errors)
  else:
    form = SignUpForm()
  return render(request, 'signup.html', {'form': form})

# Define profile page
def UserProfile(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = ProfileForm(request.POST or None, instance =current_user)

        is_host = hasattr(request.user, 'host')

        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
            return redirect('home')
        return render (request, "profile.html", {
            'form': form,
            'is_host': is_host
        })
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('login')
    
# Define logout 
def LogoutView(request):
    username = User.username
    if username != None:
        logout(request)
        return redirect('base')