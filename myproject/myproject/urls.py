from django.contrib import admin
from django.urls import path, include  # Import include to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', include('dashboard.urls')),  # Include URLs from the dashboard app
]
