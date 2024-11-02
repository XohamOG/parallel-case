# dashboard/urls.py

from django.urls import path
from .views import role_selection_view, register_view, login_view, logout_view, person_home, admin_home

urlpatterns = [
    path('', role_selection_view, name='role_selection'),  # Root URL directs to role selection page
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('person/home/', person_home, name='person_home'),
    path('admin/home/', admin_home, name='admin_home'),
]
