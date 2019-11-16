from django.contrib.auth.models import User
from rest_framework import serializers

from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Category
        fields = ('name', 'slug', 'icon', 'media',)


class StoreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Store
        fields = ('name', 'slug', 'icon', 'media',)


class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = (
            'name', 
            'slug', 
            'icon', 
            'media_raw',
            'health_raw',
            'hunger_raw',
            'sanity_raw',
            'nutrition_raw',
            'perish_raw',
            'media_cooked',
            'health_cooked',
            'hunger_cooked',
            'sanity_cooked',
            'nutrition_cooked',
            'perish_cooked',
            'category',
            'store',
            'is_active',
        )


class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Recipe
        fields = (
            'name', 
            'slug',
            'media_raw',
            'health_raw',
            'hunger_raw',
            'sanity_raw',
            'nutrition_raw',
            'perish_raw',
            'store',
            'cook_time',
            'restrictions',
            'is_active',
        )


class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.RecipeIngredient
        fields = ('name', 'recipe', 'ingredient',)
