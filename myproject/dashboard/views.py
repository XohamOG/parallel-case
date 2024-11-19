from django.shortcuts import render, redirect
from django.contrib import messages
from .firebase_utils import register_user, authenticate_user


def register_view(request):
    """Handles user registration using Firebase."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = 'user'  # Or whatever role is appropriate
        # Register user in Firebase
        result = register_user(email, password,role)
        
        if isinstance(result, str):  # If result is an error message
            messages.error(request, result)
            return redirect('register')  # Use URL name, not template path

        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')  # Use URL name, not template path

    return render(request, 'dashboard/register.html')

def login_view(request):
    """Handle user login using Firebase REST API."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user with Firebase REST API
        response = authenticate_user(email, password)

        if isinstance(response, dict) and 'idToken' in response:
            # Authentication successful
            request.session['firebase_token'] = response['idToken']
            request.session['user_email'] = email
            messages.success(request, "Logged in successfully.")
            return redirect('person')
        else:
            # Handle authentication failure
            messages.error(request, response)  # Error message from Firebase
            return redirect('login')

    return render(request, 'dashboard/login.html')



def person_home(request):
    """Protected user home page."""
    # Check if the Firebase token exists in the session
    if not request.session.get('firebase_token') or not request.session.get('user_email'):
        messages.error(request, "You must be logged in to access this page.")
        return redirect('login')  # Ensure this points to the correct URL pattern for login
    
    return render(request, 'dashboard/person_home.html')


def admin_home(request):
    """Protected admin home page."""
    if not request.session.get('firebase_token'):
        return redirect('login')

    return render(request, 'dashboard/admin_home.html')


def logout_view(request):
    """Logs the user out and clears the session."""
    request.session.flush()  # Clears all session data
    messages.success(request, "You have been logged out.")
    return redirect('login')
