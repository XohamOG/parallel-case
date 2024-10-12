#sample commit
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

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