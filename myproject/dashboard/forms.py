# dashboard/forms.py

from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
