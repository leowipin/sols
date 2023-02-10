from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

        def validate(self, data):
            user = authenticate(**data)
            if not (user and user.is_active):
                raise serializers.ValidationError('Incorrect Credentials')
            return user

#This class should be in other app
class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.SlugRelatedField(many=True, queryset=Permission.objects.all(), slug_field='codename', write_only=True)
    
    class Meta:
        model = Group
        fields = ('name', 'permissions')

class SignUpSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'group')

    def create(self, validated_data, group_name):
        group = Group.objects.get(name=group_name)
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.groups.add(group)
        user.user_permissions.set(group.permissions.all())
        user.save()
        return user

    def save(self):
        validated_data = self.validated_data
        group_name = self.context['group_name']
        return self.create(validated_data, group_name)

        