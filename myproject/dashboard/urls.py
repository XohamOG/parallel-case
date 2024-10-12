from django.urls import path
from .views import login_view, logout_view, person_home, admin_home

urlpatterns = [
    path('', login_view, name='login'),  # Root URL directs to login page
    path('logout/', logout_view, name='logout'),
    path('person/home/', person_home, name='person_home'),
    path('admin/home/', admin_home, name='admin_home'),
]