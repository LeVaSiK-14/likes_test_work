from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from django.contrib.auth import get_user_model

from accounts.serializers import UserCreateSerializer, UserSerializer
from posts.models import Posts
from posts.serializers import PostsSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserModelViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post', ], detail=True, serializer_class=PostsSerializer)
    def add_post(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            post = Posts.objects.create(
                                    author=author,
                                    title=data['title'],
                                    description=data['description'])
            serializer = self.get_serializer_class()(post)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
