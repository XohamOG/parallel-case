from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'store/product_list.html', {'products': products})

def person_home(request):
    """Protected user home page."""
    # Check if the Firebase token exists in the session
    if not request.session.get('firebase_token') or not request.session.get('user_email'):
        messages.error(request, "You must be logged in to access this page.")
        return redirect('login')  # Ensure this points to the correct URL pattern for login
    
    return render(request, 'store/person_home.html')

def catalog_view(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'store/catalog.html', {'products': products})
