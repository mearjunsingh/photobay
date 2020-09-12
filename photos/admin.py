from django.contrib import admin
from . import models


def active(modeladmin, request, queryset):
    queryset.update(active=True)

active.short_description = "Activate selected photos"

def deactive(modeladmin, request, queryset):
    queryset.update(active=False)

deactive.short_description = "Deactivate selected photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'modified_on', 'uploaded_on', 'views_count','active']
    ordering = ['title']
    list_editable = ['active']
    list_filter = ['active', 'category', 'camera', 'location']
    search_fields = ['title', 'user__username']
    actions = [active, deactive]
    date_hierarchy = 'uploaded_on'
    prepopulated_fields = {'slug' : ('title',)}
    fieldsets = (
        (None, {
            'fields' : (
                ('title'),
                ('slug'),
                ('category', 'user'),
                ('camera', 'location')
            )
        }),
        ('Image', {
            'fields' : (
                ('image', 'image_type'),
                ('description'),
                ('tags')
            )
        }),
        ('More', {
            'classes' : ('collapse'),
            'fields' : (
                ('active'),
                ('views_count')
            )
        })
    )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    ordering = ['category']
    save_as = True
    search_fields = ['category', 'slug']
    prepopulated_fields = {'slug' : ('category',)}


@admin.register(models.Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ['camera', 'slug']
    ordering = ['camera']
    save_as = True
    search_fields = ['camera', 'slug']
    prepopulated_fields = {'slug' : ('camera',)}


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['location', 'slug']
    ordering = ['location']
    save_as = True
    search_fields = ['location', 'slug']
    prepopulated_fields = {'slug' : ('location',)}


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
    ordering = ['user__username']
    list_filter = ['user', 'photo']
    search_fields = ['user__username', 'photo__title']


@admin.register(models.Save)
class SaveAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
    ordering = ['user__username']
    list_filter = ['user', 'photo']
    search_fields = ['user__username', 'photo__title']