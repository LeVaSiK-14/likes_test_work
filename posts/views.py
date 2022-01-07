from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from posts import serializers


from posts.serializers import PostsSerializer
from posts.models import Posts
from posts.mixins import LikeMixins, DisLikeMixins


class PostsModelViewsSet(LikeMixins, DisLikeMixins, ModelViewSet):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated, ]


