from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label= "Your Password", widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label= "Confirm Password", widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {'first_name': 'Your First Name', 'last_name': 'Your Last Name', 'email': 'Your Email', 'username': 'Username'}

        widgets ={'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
                  'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
                  'username': forms.TextInput(attrs={'class': 'form-control'}), 
                  'email': forms.EmailInput(attrs={'class': 'form-control'}),
                  }
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget= forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label = 'Password', widget= forms.PasswordInput(attrs={'class': 'form-control'}))