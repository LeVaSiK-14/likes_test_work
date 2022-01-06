from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from likes.models import Likes, DisLikes
from likes.serializers import LikesSerializer, DisLikesSerializer


class LikeMixins:
    
    @action(methods=['post'], detail=True, serializer_class=LikesSerializer)
    def set_like(self, request, *args, **kwargs):
        post = self.get_object()
        author = request.user
        like = Likes.objects.filter(post=post, author=author)
        dislike = DisLikes.objects.filter(post=post, author=author)
        if like.exists():
            like.delete()
            post.likes -= 1
            post.save()
            return Response({'Message': "Вы убрали лайк"}, status=status.HTTP_200_OK)
        
        else:
            if dislike.exists():
                dislike.first().delete()
                post.dislikes -= 1

            Likes.objects.create(author=author, post=post)
            post.likes += 1
            post.save()
            return Response({"Message": "Вы поставили лайк"}, status=status.HTTP_201_CREATED)


class DisLikeMixins:
    
    @action(methods=['post'], detail=True, serializer_class=DisLikesSerializer)
    def set_dislike(self, request, *args, **kwargs):
        post = self.get_object()
        author = request.user
        like = Likes.objects.filter(post=post, author=author)
        dislike = DisLikes.objects.filter(post=post, author=author)
        if dislike.exists():
            dislike.delete()
            post.dislikes -= 1
            post.save()
            return Response({'Message': "Вы убрали дизлайк"}, status=status.HTTP_200_OK)
        
        else:
            if like.exists():
                like.first().delete()
                post.likes -= 1

            DisLikes.objects.create(author=author, post=post)
            post.dislikes += 1
            post.save()
            return Response({"Message": "Вы поставили дизлайк"}, status=status.HTTP_201_CREATED)


