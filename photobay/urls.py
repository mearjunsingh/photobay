"""photobay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

from photos.views import (
    index_page_view,
    single_page_view,
    profile_public_page_view,
)

from users.views import (
    login_page_view,
    logout_page_view,
    signup_page_view,
)

urlpatterns = [
    path('', index_page_view, name='index'),
    path('browse/', include('photos.urls')),
    path('login/', login_page_view, name='login'),
    path('logout/', logout_page_view, name='logout'),
    path('signup/', signup_page_view, name='signup'),
    path('dashboard/', include('users.urls')),
    path('photobay-admin/', admin.site.urls),
    path('<str:username>/', profile_public_page_view, name='public_profile'),
    path('<str:username>/<str:slug>/', single_page_view, name='single'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Photobay Admin Panel'
admin.site.site_title = 'Photobay'
admin.site.index_title = "Photobay's Database"