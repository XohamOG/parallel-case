# dashboard/urls.py

from django.urls import path
from .views import register_view, login_view, logout_view, admin_home
from store.views import person_home

urlpatterns = [
    path('',  login_view, name='home_new'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('store', person_home, name='store'),
    path('admin/home/', admin_home, name='admin_home'),
]
