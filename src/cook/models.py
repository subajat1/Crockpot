from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    media = models.CharField(max_length=1024, null=True, blank=True)
    icon = models.CharField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Store(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=1024, null=True, blank=True)
    media = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Store, self).save(*args, **kwargs)


class Ingredient(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=1024, null=True, blank=True)
    
    media_raw = models.CharField(max_length=1024, null=True, blank=True)
    health_raw = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    hunger_raw = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    sanity_raw = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    nutrition_raw = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    perish_raw = models.DecimalField(max_digits=7, decimal_places=3, blank=True)

    media_cooked = models.CharField(max_length=1024, null=True, blank=True)
    health_cooked = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    hunger_cooked = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    sanity_cooked = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    nutrition_cooked = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    perish_cooked = models.DecimalField(max_digits=7, decimal_places=3, blank=True)

    category = models.ForeignKey(Category, related_name='ing_category', on_delete=models.SET_NULL, null=True, blank=True)
    store = models.ManyToManyField('Store', related_name='ing_store')
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    log = models.TextField(blank=True, null=True, default='')

    class Meta:
        ordering = ['name']
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)    


class Recipe(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    slug = models.SlugField(unique=True)
    
    media = models.CharField(max_length=1024, null=True, blank=True)
    health = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    hunger = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    sanity = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    nutrition = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    perish = models.DecimalField(max_digits=7, decimal_places=3, blank=True)
    store = models.ManyToManyField('Store', related_name='recipe_store')
    cook_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    restrictions = models.CharField(max_length=1024, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    log = models.TextField(blank=True, null=True, default='')

    class Meta:
        ordering = ['name']
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

class RecipeIngredient(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, related_name='ri_recipe', on_delete=models.SET_NULL, null=True, blank=True)
    ingredient = models.ForeignKey(Ingredient, related_name='ri_ingredient', on_delete=models.SET_NULL, null=True, blank=True)
