from rest_framework import serializers

from posts.models import Posts


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Posts
        fields = [
            'id', 'author', 'title', 'description', 
            'created_at', 'likes', 'dislikes', 
        ]
        read_only_fields = ['created_at', 'likes', 'dislikes', ]
        