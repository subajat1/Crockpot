from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import permissions, renderers, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import models, serializers

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)

class StoreViewSet(viewsets.ModelViewSet):
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreSerializer
    authentication_classes = (TokenAuthentication,)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = (TokenAuthentication,)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
    authentication_classes = (TokenAuthentication,)

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    authentication_classes = (TokenAuthentication,)

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = models.RecipeIngredient.objects.all()
    serializer_class = serializers.RecipeIngredientSerializer
    authentication_classes = (TokenAuthentication,)
