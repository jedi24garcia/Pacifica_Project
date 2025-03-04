from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.UserLogin, name='login'),
  path('signup/', views.UserSignUp, name='signup'),
  path('logout/', views.LogoutView, name='logout'),
  path('user_profile/', views.UserProfile, name='user_profile'),
]