from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import permissions, renderers, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import serializers

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)
