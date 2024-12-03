# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

from store.views import person_home, product_list
urlpatterns = [
    path('store/',person_home,name = 'store_home'),  # Include store URLs
]
