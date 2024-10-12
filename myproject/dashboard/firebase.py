# dashboard/firebase.py

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('D:\downloads\template-13d9d-firebase-adminsdk-1gi4r-ebac398443.json')  # Update this path
firebase_admin.initialize_app(cred)
