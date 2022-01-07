from django.urls import path
from likes.views import LikesModelViewSet, DisLikesModelViewSet


urlpatterns = [
    path('list-likes/', LikesModelViewSet.as_view(), name='list_likes'),
    path('list-dislikes/', DisLikesModelViewSet.as_view(), name='list_dislikes'),
]