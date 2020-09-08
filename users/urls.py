from django.urls import path

from .views import (
    dashboard_page_view,
    upload_page_view,
    edit_page_view,
    delete_page_view,
    edit_profile_page_view,
    deactivate_profile_page_view,
    change_password_view,
)

urlpatterns = [
    path('', dashboard_page_view, name='dashboard'),
    path('upload/', upload_page_view, name='upload'),
    path('edit/<str:slug>/', edit_page_view, name='edit'),
    path('delete/', delete_page_view, name='delete'),
    path('profile/', edit_profile_page_view, name='edit_profile'),
    path('profile/password/', change_password_view, name='change_password'),
    path('profile/deactivate/', deactivate_profile_page_view, name='deactivate_profile'),
]