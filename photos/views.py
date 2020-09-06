from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def index_page_view(request):
    return render(request, 'index.html')


def browse_page_view(request):
    return render(request, 'discover.html')


def single_page_view(request, username, slug):
    return render(request, 'single.html')


def profile_public_page_view(request, username):
    data = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'users/userpublic.html')