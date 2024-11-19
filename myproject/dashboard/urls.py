# dashboard/urls.py

from django.urls import path
from .views import register_view, login_view, logout_view, person_home, admin_home

urlpatterns = [
    path('',  login_view, name='home_new'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('person', person_home, name='person'),
    path('admin/home/', admin_home, name='admin_home'),
]
