from django.urls import path
from .views import login_view, logout_view, person_home, admin_home, firebase_login_view

urlpatterns = [
    path('', login_view, name='login'),  # Root URL directs to login page
    path('logout/', logout_view, name='logout'),
    path('person/home/', person_home, name='person_home'),
    path('admin/home/', admin_home, name='admin_home'),
    path('api/login/', firebase_login_view, name='firebase_login'),  # New API endpoint for login
]
