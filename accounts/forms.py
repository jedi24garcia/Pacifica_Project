from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
  User_First_Name = forms.CharField(max_length=40, required=True, help_text="Enter your first name")
  User_Last_Name = forms.CharField(max_length=40, required=True, help_text="Enter your last name")

  class Meta:
    model = User
    fields = ("username", "User_First_Name", "User_Last_Name", "password1", "password2")

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):

    phone_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}), required=False)
    email_address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}), required=False)

    class Meta:
      model = Profile
      fields =( 'phone_number', 'email_address')