from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status

from django.contrib.auth import get_user_model

from accounts.serializers import UserCreateSerializer

User = get_user_model()

class UserCreateAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

