from django.urls import path

from .views import (
    browse_page_view,
    cameras_page_view,
    artists_page_view,
    locations_page_view,
)

urlpatterns = [
    path('', browse_page_view, name='browse'),
    path('cameras/', cameras_page_view, name='camera'),
    path('locations/', locations_page_view, name='location'),
    path('artists/', artists_page_view, name='artists'),
]