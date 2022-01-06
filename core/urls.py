from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="LIKES API",
        default_version='v1',
        description="Likes api",
        terms_of_service="",
        contact=openapi.Contact(email="lev201611@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    path('api/swagger/', schema_view.with_ui(), name='schema-json'),
]