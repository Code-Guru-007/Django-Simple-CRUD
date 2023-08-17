from .models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "avatar" , "bio", "can_hire", "country", "email", "username", "password", "first_name", "is_public", "last_name", "phone", "role", "state", "timezone"]