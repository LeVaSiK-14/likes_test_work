from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.serializers import PostsSerializer
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    posts = PostsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'last_login']


class UserRegistartionSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError('Password is too short')
        elif len(value) > 20:
            raise ValidationError('Password is too long')
        else: 
            return value

    def create(self, validated_data):

        username = validated_data['username']
        password = validated_data['password']

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user