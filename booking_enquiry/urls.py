from django.urls import path
from .views import generate_kayak_url_view

urlpatterns = [
    path('hotel_url/', generate_kayak_url_view, name='hotel_url'),  # Use path for function-based views
]
