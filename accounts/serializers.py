from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import exceptions

User = get_user_model()

class UserCreateSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=127)
    password = serializers.CharField(max_length=127)
    password_repeat = serializers.CharField(max_length=127)


    def create(self, validated_data):
        
        username = validated_data['username']
        password = validated_data['password']
        password_repeat = validated_data['password_repeat']

        if len(password) <= 8:
            raise exceptions.ValidationError({"Password": 'Password is too short'})
        else:
            if password == password_repeat:
                user = User.objects.create(username=username)
                user.set_password(password)
                user.is_active = False
                user.save()
                return user
            else:
                raise exceptions.ValidationError({"Password": 'Passwords do not match'})
