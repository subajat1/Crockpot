from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'media',
        'slug',
    )
admin.site.register(models.Category, CategoryAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'media',
        'slug',
    )
admin.site.register(models.Store, StoreAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'category',
        'is_active',
    )
admin.site.register(models.Ingredient, IngredientAdmin)

class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'media',
        'slug',
        'cook_time',
        'is_active',
    )
admin.site.register(models.Recipe, RecipeAdmin)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'recipe',
        'ingredient',
    )
admin.site.register(models.RecipeIngredient, RecipeIngredientAdmin)