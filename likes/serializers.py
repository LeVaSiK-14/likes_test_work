from rest_framework import serializers
from likes.models import Likes, DisLikes

class LikesSerializer(serializers.ModelSerializer):

    post = serializers.ReadOnlyField(source='post.title')
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:

        model = Likes
        fields = ['id', 'post', 'author', 'created_at', ]
        read_only_fields = ['created_at', ]