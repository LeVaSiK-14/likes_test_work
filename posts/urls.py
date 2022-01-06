from rest_framework.routers import SimpleRouter
from posts.views import PostsModelViewsSet

router = SimpleRouter()

router.register('posts', PostsModelViewsSet)

urlpatterns = []

urlpatterns += router.urls