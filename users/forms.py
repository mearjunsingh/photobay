from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Username',
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Password',
            }
        ))


class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(label='Enter First Name', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter First Name',
            }
        ))
    last_name = forms.CharField(label='Enter Last Name', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Last Name',
            }
        ))
    email = forms.EmailField(label='Enter Email', widget=forms.EmailInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Email',
            }
        ))
    username = forms.CharField(label='Choose Username', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Choose Username',
            }
        ))
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Password',
            }
        ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Password Again',
            }
        ))
        
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']