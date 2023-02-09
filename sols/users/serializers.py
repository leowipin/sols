from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth import authenticate

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

        def validate(self, data):
            user = authenticate(**data)
            if not (user and user.is_active):
                raise serializers.ValidationError('Incorrect Credentials')
            return user
    