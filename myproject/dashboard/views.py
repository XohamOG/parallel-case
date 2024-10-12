# dashboard/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from firebase_admin import auth
import json

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            return JsonResponse({"success": True, "message": "User created successfully."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = auth.get_user_by_email(email)
            # Simulate the login check (Firebase doesn't support password login directly)
            return redirect('home')
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')
