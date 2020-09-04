from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_page_view(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                User = authenticate(username=username, password=password)
                login(request, User)
                return redirect('index')
        else:
            form = UserLoginForm(request.POST or None)
        return render(request, 'login.html', {'form' : form})


def signup_page_view(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('dashboard')
    else:
        form = UserSignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully. Please Login to Continue.')
            return redirect('login')
        return render(request, 'register.html', {'form': form})



def dashboard_page_view(request):
    return render(request, 'register.html')