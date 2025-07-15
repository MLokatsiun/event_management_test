from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    """
    POST /api/users/register/

    Allows a new user to register by providing username, email, and password.

    Request Body (application/json):
    {
        "username": "string",
        "email": "user@example.com",
        "password": "string"
    }

    Responses:
    201 Created:
    {
        "id": 1,
        "username": "string",
        "email": "user@example.com"
    }

    400 Bad Request: Validation errors if fields are missing or invalid.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

