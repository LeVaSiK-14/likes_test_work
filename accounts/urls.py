from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import SimpleRouter
from django.urls import path

from accounts.views import (
                            UserModelViewSet, 
                            RegisterGenericAPIView)

router = SimpleRouter()

router.register('users', UserModelViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegisterGenericAPIView.as_view(), name='registartion')
]

urlpatterns += router.urls