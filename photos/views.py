from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Like, Save, Camera, Location
from django.core.paginator import Paginator
from django.db.models import Q
import re
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
#from users.custom_defs import get_exif_data
# Create your views here.

#completed
def index_page_view(request):
    home = get_object_or_404(Photo, id=6)
    data = Photo.objects.filter(active=True).order_by('-views_count')[:20]
    return render(request, 'index.html', {'home' : home, 'data' : data})

#completed
def browse_page_view(request):
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        b_url = '?search=' + search_term + '&'
        photos_list = Photo.objects.filter(active=True).filter(
                Q(title__icontains = search_term) | 
                Q(tags__icontains = search_term) | 
                Q(description__icontains = search_term)).order_by('-uploaded_on')
    elif 'category' in request.GET:
        search_term = request.GET.get('category')
        b_url = '?category=' + search_term + '&'
        photos_list = Photo.objects.filter(active=True).filter(category__slug=search_term).order_by('-uploaded_on')
    elif 'camera' in request.GET:
        search_term = request.GET.get('camera')
        b_url = '?camera=' + search_term + '&'
        photos_list = Photo.objects.filter(active=True).filter(camera__slug=search_term).order_by('-uploaded_on')
    elif 'location' in request.GET:
        search_term = request.GET.get('location')
        b_url = '?location=' + search_term + '&'
        photos_list = Photo.objects.filter(active=True).filter(location__slug=search_term).order_by('-uploaded_on')
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

#completed
def single_page_view(request, username, slug):
    data = get_object_or_404(Photo, user__username=username, slug=slug, active=True)
    data.views_count += 1
    data.save()
    liked, saved = False, False
    if request.user.is_authenticated:
    	liked = True if data.like_set.filter(user=request.user).count() > 0 else False
    	saved = True if data.save_set.filter(user=request.user).count() > 0 else False
    if 'like' in request.POST:
        if request.user.is_authenticated:
            like = Like.objects.filter(user=request.user, photo=data)
            if like.exists():
                like.delete()
            else:
                temp = Like(user=request.user, photo=data)
                temp.save()
        else:
            messages.error(request, 'You must login first.')
    if 'save' in request.POST:
        if request.user.is_authenticated:
            save = Save.objects.filter(user=request.user, photo=data)
            if save.exists():
                save.delete()
            else:
                temp2 = Save(user=request.user, photo=data)
                temp2.save()
        else:
            messages.error(request, 'You must login first.')
    image_tags = data.tags
    image_tags = re.split(', |,', image_tags)
    #try:
    #    exif = get_exif_data(data.image)
    #except:
    #    exif = None
    author = Photo.objects.filter(user__username=username).filter(active=True).order_by('-uploaded_on')[:4]
    related = Photo.objects.filter(category=data.category).filter(active=True).order_by('-uploaded_on')[:4]
    return render(request, 'single.html', {'image_tags' : image_tags, 'data' : data, 'liked' : liked, 'saved' : saved, 'author' : author, 'related' : related})#, 'exif' : exif})

#completed
def profile_public_page_view(request, username):
    person = get_object_or_404(User, username=username, is_active=True)
    home = get_object_or_404(Photo, id=6)
    photos_list = Photo.objects.filter(active=True).filter(user=person).order_by('-uploaded_on')
    b_url = '?'
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
        return render(request, 'users/userpublic.html', {'home' : home, 'person' : person, 'data' : data, 'base_url' : b_url})
    else:
        return render(request, 'users/userpublic.html', {'home' : home, 'person' : person, 'no_posts_found' : True, 'base_url' : b_url})

#completed
def cameras_page_view(request):
    data_list = Camera.objects.all().order_by('camera')
    b_url = '?'
    if data_list.count() != 0:
        paginator = Paginator(data_list, 20)
        if 'page' in request.GET:
            q = request.GET['page']
            if q is not None and q != '' and q != '0':
                page_number = request.GET.get('page')
            else:
                page_number = 1
        else:
            page_number = 1
        data = paginator.get_page(page_number)
    return render(request, 'explore_camera.html', {'data' : data, 'base_url' : b_url})

#completed
def artists_page_view(request):
    data_list = User.objects.filter(is_active=True).order_by('-date_joined')
    b_url = '?'
    if data_list.count() != 0:
        paginator = Paginator(data_list, 20)
        if 'page' in request.GET:
            q = request.GET['page']
            if q is not None and q != '' and q != '0':
                page_number = request.GET.get('page')
            else:
                page_number = 1
        else:
            page_number = 1
        data = paginator.get_page(page_number)
    return render(request, 'explore_users.html', {'data' : data, 'base_url' : b_url})

#completed
def locations_page_view(request):
    data_list = Location.objects.all().order_by('location')
    b_url = '?'
    if data_list.count() != 0:
        paginator = Paginator(data_list, 20)
        if 'page' in request.GET:
            q = request.GET['page']
            if q is not None and q != '' and q != '0':
                page_number = request.GET.get('page')
            else:
                page_number = 1
        else:
            page_number = 1
        data = paginator.get_page(page_number)
    return render(request, 'explore_location.html', {'data' : data, 'base_url' : b_url})