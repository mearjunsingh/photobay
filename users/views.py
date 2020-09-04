from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
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
                messages.success(request, 'You are logged in.')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
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
            messages.success(request, 'Account Created Successfully.')
            return redirect('login')
        return render(request, 'register.html', {'form': form})


def logout_page_view(request):
    if not request.user.is_authenticated:
        raise Http404()
    else:
        logout(request)
        messages.warning(request, 'You are logged out.')
        return redirect('index')

@login_required()
def dashboard_page_view(request):
    return render(request, 'users/user.html')