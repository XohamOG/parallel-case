import firebase_admin
from firebase_admin import credentials, auth
import requests

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(r'D:\parallel-case\template-13d9d-firebase-adminsdk-1gi4r-b32f77d41e.json')
    firebase_admin.initialize_app(cred)

def register_user(email, password, role):
    """
    Registers a user in Firebase with the specified email, password, and role.
    """
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        # Optionally, store additional user information (e.g., role) in Firebase
        return user
    except Exception as e:
        return str(e)


def authenticate_user(email, password):
    """
    Authenticate a user with Firebase using REST API.
    """
    # Firebase REST API URL for signing in users
    FIREBASE_AUTH_URL = r"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDFo70_K4d7rywqcXGw3pwY-XnRzwNZxpo"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    try:
        # Send a POST request to Firebase Authentication API
        response = requests.post(FIREBASE_AUTH_URL, json=payload)
        response_data = response.json()

        # If the response contains an ID token, authentication succeeded
        if 'idToken' in response_data:
            return response_data  # Success response
        else:
            # Firebase will return an error message
            return response_data.get("error", {}).get("message", "Authentication failed")
    except requests.RequestException as e:
        # Handle network-related errors
        return str(e)