from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def index_page_view(request):
    home = get_object_or_404(Photo, id=6)
    return render(request, 'index.html', {'home' : home})


def browse_page_view(request):
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        b_url = '?search=' + search_term + '&'
        photos_list = Photo.objects.filter(active=True).filter(
                Q(title__icontains = search_term) | 
                Q(tags__icontains = search_term) | 
                Q(category__category__icontains = search_term) | 
                Q(user__username__icontains = search_term) | 
                Q(camera__camera__icontains = search_term) | 
                Q(location__location__icontains = search_term)).order_by('-uploaded_on')
    elif 'category' in request.GET:
        search_term = request.GET.get('category')
        b_url = '?category=' + search_term + '&'
        photos_list = Photo.objects.filter(active=True).filter(category__slug=search_term).order_by('-uploaded_on')
    else:
        b_url = '?'
        photos_list = Photo.objects.filter(active=True).order_by('-uploaded_on')
    if photos_list.count() != 0:
        paginator = Paginator(photos_list, 20)
        if 'page' in request.GET:
            q = request.GET['page']
            if q is not None and q != '' and q != '0':
                page_number = request.GET.get('page')
            else:
                page_number = 1
        else:
            page_number = 1
        data = paginator.get_page(page_number)
        return render(request, 'discover.html', {'data' : data, 'base_url' : b_url})
    else:
        return render(request, 'discover.html', {'no_posts_found' : True})


def single_page_view(request, username, slug):
    return render(request, 'single.html')


def profile_public_page_view(request, username):
    data = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'users/userpublic.html')