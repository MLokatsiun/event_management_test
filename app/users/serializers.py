from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Django User model to handle user creation.

    Fields:
        - id: Read-only user ID.
        - username: User's username.
        - email: User's email address.
        - password: Write-only password field used for user creation.

    Methods:
        - create: Overrides default to use Django's create_user method, which
          properly hashes the password and creates the user instance.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        """
        Create and return a new User instance using validated data.
        Password is hashed internally by create_user.
        """
        user = User.objects.create_user(**validated_data)
        return user