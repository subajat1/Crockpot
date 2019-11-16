from django.contrib import admin

from . import models

class BenefitAdmin(admin.ModelAdmin):
    list_display = (
        'health',
        'hunger',
        'sanity',
        'nutrition',
        'perish',
    )
admin.site.register(models.Benefit, BenefitAdmin)


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
        'media',
        'slug',
        'category',
        'is_active'
    )
admin.site.register(models.Ingredient, IngredientAdmin)

class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'media',
        'slug',
        'benefit',
        'cook_time',
        'is_active'
    )
admin.site.register(models.Recipe, RecipeAdmin)
