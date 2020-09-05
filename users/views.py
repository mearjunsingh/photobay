from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserSignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from photos.forms import UploadForm, EditForm
from photos.models import Photo, Camera, Location
from pathlib import Path
from .unique_slug import unique_slug
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
                    next_url = request.POST.get('next')
                    return redirect(next_url)
                else:
                    return redirect('index')
        else:
            form = UserLoginForm()
            if 'next' in request.GET:
                messages.error(request, 'You must login first.')
        return render(request, 'login.html', {'form' : form})


def signup_page_view(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('dashboard')
    else:
        form = UserSignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
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


@login_required()
def upload_page_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():

            temp, temp2 = request.POST.get('photo_camera'), request.POST.get('photo_location')
            if not Camera.objects.filter(camera=temp).exists():
                cam_obj = Camera(camera=temp, slug=unique_slug(Camera, temp))
                cam_obj.save()
            else:
                cam_obj = get_object_or_404(Camera, camera=temp)
            if not Location.objects.filter(location=temp2).exists():
                loc_obj = Location(location=temp2, slug=unique_slug(Location, temp2))
                loc_obj.save()
            else:
                loc_obj = get_object_or_404(Location, location=temp2)

            data = form.save(commit=False)
            data.slug = unique_slug(Photo, data.title)
            data.user = request.user
            data.image_type = data.image.name.split('.')[-1].upper()
            data.camera = cam_obj
            data.location = loc_obj
            data.save()
            messages.success(request, 'Photo uploaded successfully.')
            return redirect('dashboard')
    else:
        form = UploadForm()
    return render(request, 'users/upload_edit.html', {'form' : form, 'head' : 'Upload New Photo', 'button' : 'Upload'})


@login_required()
def edit_profile_page_view(request):
    return render(request, 'users/useraction.html')


@login_required()
def delete_page_view(request):
    if request.method == 'POST':
        data = get_object_or_404(Photo, slug=request.POST.get('slug'), active=True)
        data.active = False
        data.save()
        messages.warning(request, 'Photo deleted successfully.')
        return redirect('dashboard')
    else:
        raise Http404()


@login_required()
def edit_page_view(request, slug):
    if request.method == 'POST':
        instance = get_object_or_404(Photo, slug=slug, active=True)
        form = EditForm(request.POST, instance=instance)
        if form.is_valid():

            temp, temp2 = request.POST.get('photo_camera'), request.POST.get('photo_location')
            if not Camera.objects.filter(camera=temp).exists():
                cam_obj = Camera(camera=temp, slug=unique_slug(Camera, temp))
                cam_obj.save()
            else:
                cam_obj = get_object_or_404(Camera, camera=temp)
            if not Location.objects.filter(location=temp2).exists():
                loc_obj = Location(location=temp2, slug=unique_slug(Location, temp2))
                loc_obj.save()
            else:
                loc_obj = get_object_or_404(Location, location=temp2)

            data = form.save(commit=False)
            data.camera = cam_obj
            data.location = loc_obj
            data.save()
            messages.success(request, 'Photo uploaded successfully.')
            return redirect('dashboard')
    else:
        data = get_object_or_404(Photo, slug=slug, active=True)
        print(data)
        param = {
            'title' : data.title,
            'category' : data.category,
            'photo_camera' : data.camera,
            'photo_location' : data.location,
            'tags' : data.tags
        }
        form = EditForm(initial=param)
    return render(request, 'users/upload_edit.html', {'form' : form, 'head' : 'Edit Photo Details', 'button' : 'Update', 'slug' : slug})