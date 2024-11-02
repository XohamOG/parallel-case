# dashboard/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm  # Assuming you have this form
from firebase_admin import auth  # Firebase auth for user management

def role_selection_view(request):
    return render(request, 'dashboard/role_selection.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Get the selected role (admin or person)

        # Create the user in Firebase (you can customize this part)
        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            # Here you can save the role in your user model
            # Assuming you have a UserProfile model linked to Django's User model
            # UserProfile.objects.create(user=user, is_person=(role == 'person'), is_admin=(role == 'admin'))
            return redirect('login')  # Redirect to login after successful registration
        except Exception as e:
            return render(request, 'dashboard/register.html', {'error': str(e)})

    return render(request, 'dashboard/register.html')

def login_view(request):
    form = UserLoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        # Redirect based on role (assuming you have a way to identify roles)
        if hasattr(user, 'is_person') and user.is_person:
            return redirect('person_home')
        elif hasattr(user, 'is_admin') and user.is_admin:
            return redirect('admin_home')
        else:
            return redirect('login')  # Fallback

    return render(request, 'dashboard/login.html', {'form': form})

@login_required
def person_home(request):
    return render(request, 'dashboard/person_home.html')

@login_required
def admin_home(request):
    return render(request, 'dashboard/admin_home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
