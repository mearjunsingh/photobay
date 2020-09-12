from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
# from .models import UserProfile, BannedUsernames
from .forms import UserSignupForm, UserEditForm

def active(modeladmin, request, queryset):
    queryset.update(is_active=True)

active.short_description = "Activate selected users"

def deactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

deactive.short_description = "Deactivate selected users"


@admin.register(models.UserProfile)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'date_joined','is_active']
    ordering = ['username']
    list_editable = ['is_active']
    list_filter = ['is_active', 'profession', 'address']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    actions = [active, deactive]
    date_hierarchy = 'date_joined'
    add_form = UserSignupForm
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {
            'fields' : (
                ('username'),
                ('first_name'),
                ('last_name'),
                ('email'),
                ('profile_picture')
            )
        }),
        ('Personal Details', {
            'fields' : (
                ('profession'),
                ('address'),
                ('dob')
            )
        }),
        ('Links', {
            'fields' : (
                ('donate'),
                ('fb_username'),
                ('tw_username'),
                ('in_username')
            )
        }),
        ('More', {
            'fields' : (
                ('is_active'),
                ('is_staff'),
                ('is_superuser'),
                ('last_login'),
                ('date_joined')
            )
        }),
        ('Permissions', {
            'fields' : (
                ('groups'),
                ('user_permissions')
            )
        })
    )


@admin.register(models.BannedUsernames)
class BannedUsernamesAdmin(admin.ModelAdmin):
    list_display = ['uname']
    ordering = ['uname']
    search_fields = ['uname']