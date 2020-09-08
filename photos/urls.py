from django.urls import path

from .views import (
    browse_page_view,
)

urlpatterns = [
    path('', browse_page_view, name='browse'),
    path('cameras/', browse_page_view, name='camera'),
    path('locations/', browse_page_view, name='location'),
    path('artists/', browse_page_view, name='artists'),
]