# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

from store.views import person_home, catalog_view
urlpatterns = [
    path('store/',person_home,name = 'store_home'),
      path('catalog',catalog_view,name = 'catalog'),   # Include store URLs
]
