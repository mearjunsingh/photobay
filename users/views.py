from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserSignupForm, UserEditForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from photos.forms import UploadForm, EditForm
from photos.models import Photo, Camera, Location
from .custom_defs import unique_slug, get_or_create_object, rename_on_delete
from django.core.paginator import Paginator
from django.db.models import Q
User = get_user_model()
# Create your views here.

#completed
def login_page_view(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in.')
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user_cre = authenticate(username=username, password=password)
                login(request, user_cre)
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

#completed
def signup_page_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in.')
        return redirect('dashboard')
    else:
        form = UserSignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
        return render(request, 'register.html', {'form': form})

#completed
def logout_page_view(request):
    if not request.user.is_authenticated:
        raise Http404()
    else:
        logout(request)
        messages.error(request, 'You are logged out.')
        return redirect('index')


@login_required() #completed
def dashboard_page_view(request):
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        b_url = '?search=' + search_term + '&'
        photos_list = Photo.objects.filter(active=True).filter(user=request.user).filter(
                Q(title__icontains = search_term) | 
                Q(tags__icontains = search_term) | 
                Q(category__category__icontains = search_term) | 
                Q(camera__camera__icontains = search_term) | 
                Q(location__location__icontains = search_term)).order_by('-uploaded_on')
    else:
        b_url = '?'
        photos_list = Photo.objects.filter(active=True).filter(user=request.user).order_by('-uploaded_on')
    if photos_list.count() != 0:
        paginator = Paginator(photos_list, 6)
        if 'page' in request.GET:
            q = request.GET['page']
            if q is not None and q != '' and q != '0':
                page_number = request.GET.get('page')
            else:
                page_number = 1
        else:
            page_number = 1
        data = paginator.get_page(page_number)
        return render(request, 'users/user.html', {'data' : data, 'base_url' : b_url})
    else:
        return render(request, 'users/user.html', {'no_posts_found' : True})


@login_required() #completed
def upload_page_view(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        temp, temp2 = request.POST.get('photo_camera'), request.POST.get('photo_location')
        data = form.save(commit=False)
        data.slug = unique_slug(Photo, data.title)
        data.user = request.user
        data.image_type = data.image.name.split('.')[-1].upper()
        data.camera = get_or_create_object(temp, Camera)
        data.location = get_or_create_object(temp2, Location)
        data.save()
        messages.success(request, 'Photo uploaded successfully.')
        return redirect('dashboard')
    return render(request, 'users/upload_edit.html', {'form' : form, 'head' : 'Upload New Photo', 'button' : 'Upload Photo'})


@login_required() #completed
def edit_profile_page_view(request):
    instance = get_object_or_404(User, username=request.user.username, is_active=True)
    form = UserEditForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('dashboard')
    return render(request, 'users/upload_edit.html', {'form' : form, 'head' : 'Edit Profile', 'button' : 'Update Changes', 'secret_key' : True})


@login_required() #completed
def delete_page_view(request):
    if request.method == 'POST':
        data = get_object_or_404(Photo, slug=request.POST.get('slug'), user=request.user, active=True)
        data.active = False
        data.image = rename_on_delete(data.image)
        data.save()
        messages.error(request, 'Photo deleted successfully.')
        return redirect('dashboard')
    else:
        raise Http404()


@login_required() #completed
def edit_page_view(request, slug):
    instance = get_object_or_404(Photo, slug=slug, active=True)
    form = EditForm(request.POST or None, instance=instance)
    if form.is_valid():
        temp, temp2 = request.POST.get('photo_camera'), request.POST.get('photo_location')
        data = form.save(commit=False)
        data.camera = get_or_create_object(temp, Camera)
        data.location = get_or_create_object(temp2, Location)
        data.save()
        messages.success(request, 'Photo updated successfully.')
        return redirect('dashboard')
    else:
        param = {
            'title' : instance.title,
            'category' : instance.category,
            'description' : instance.description,
            'photo_camera' : instance.camera,
            'photo_location' : instance.location,
            'tags' : instance.tags
        }
        form = EditForm(initial=param)
    return render(request, 'users/upload_edit.html', {'form' : form, 'head' : 'Edit Photo Details', 'button' : 'Update Changes', 'slug' : slug})


@login_required() #completed
def change_password_view(request):
    form = ChangePasswordForm(user=request.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        messages.success(request, 'Password changed successfully.')
        return redirect('dashboard')
    return render(request, 'users/upload_edit.html', {'form' : form, 'head' : 'Change Password', 'button' : 'Update Changes'})


@login_required() #completed
def deactivate_profile_page_view(request):
    if request.method == 'POST':
        data = get_object_or_404(User, username=request.user.username, is_active=True)
        photos = Photo.objects.filter(user=request.user).filter(active=True)
        likes = request.user.like_set.all()
        data.is_active = False
        photos.update(active=False)
        data.save()
        messages.error(request, 'Profile deactivated successfully.')
        return redirect('index')
    else:
        raise Http404()