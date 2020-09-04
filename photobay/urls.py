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
from django.urls import path
from photos.views import (
    index_page_view,
)
from users.views import (
    login_page_view,
    signup_page_view,
    dashboard_page_view,
)

urlpatterns = [
    path('', index_page_view, name='index'),
    path('dashboard/', dashboard_page_view, name='dashboard'),
    path('login/', login_page_view, name='login'),
    path('signup/', signup_page_view, name='signup'),
    path('admin/', admin.site.urls),
]
