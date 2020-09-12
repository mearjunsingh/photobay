from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, BannedUsernames
from .forms import UserSignupForm


class MyUserAdmin(UserAdmin):
    #add_form = UserSignupForm
    #form = CustomUserChangeForm
    model = UserProfile
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = UserAdmin.fieldsets + (
            ('Personal_info', {'fields': ('profile_picture', 'profession', 'address', 'dob', 'donate', 'fb_username', 'tw_username', 'in_username')}),
    )
    # # (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    # list_display = ['username', 'first_name', 'last_name', 'email', 'is_active'] #list_view
    # fieldsets = UserAdmin.fieldsets + (
    #         (None, {'fields': ('profession', 'address', 'dob', 'fb_username', 'tw_username', 'in_username')}),
    # )


admin.site.register(UserProfile, MyUserAdmin)
admin.site.register(BannedUsernames)