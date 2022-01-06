from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.serializers import PostsSerializer
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    posts = PostsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
