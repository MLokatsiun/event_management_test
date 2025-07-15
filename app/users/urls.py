from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
]

"""
URL Patterns:
- POST /register/ : Endpoint to register a new user using UserSerializer.

This URL is connected to the RegisterView which handles user registration requests.
"""