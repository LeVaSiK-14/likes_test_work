from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from posts.serializers import PostsSerializer
from posts.models import Posts
from posts.mixins import LikeDislikeMixins


class PostsModelViewsSet(LikeDislikeMixins, ModelViewSet):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated, ]


