from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework import status

from likes.models import Likes, DisLikes
from likes.serializers import LikesSerializer, DisLikesSerializer


class LikeDislikeMixins:

    @action(methods=['post'], detail=True, serializer_class=LikesSerializer)
    def set_like(self, request, *args, **kwargs):
        post = self.get_object()
        author = request.user
        like = Likes.objects.filter(post=post, author=author)
        dislike = DisLikes.objects.filter(post=post, author=author)
        if like.exists():
            like.delete()
            post.likes -+ 1
            post.save()
            return Response({'Message': "Вы убрали лайк"})
        
        else:
            if dislike.exists():
                dislike.first().delete()
                post.dislikes -= 1
                
            Likes.objects.create(user=author, post=post)
            post.likes += 1
            post.save()
            return Response({"Message": "Вы поставили лайк"})


