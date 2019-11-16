from django.db import models
from django.utils.text import slugify


class Benefit(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    media = models.CharField(max_length=1024, null=True, blank=True)
    health = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    hunger = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    sanity = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    nutrition = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    perish = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    class Meta:
        ordering = ['health', 'hunger', 'sanity', 'nutrition', '-perish']
        verbose_name = 'Benefit'
        verbose_name_plural = 'Benefits'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    media = models.CharField(max_length=1024, null=True, blank=True)
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
    media = models.CharField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(unique=True)

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
    media = models.CharField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(unique=True)
    benefit_raw = models.ForeignKey(Benefit, related_name='ing_benefit_raw', on_delete=models.SET_NULL, null=True, blank=True)
    benefit_cooked = models.ForeignKey(Benefit, related_name='ing_benefit_cooked', on_delete=models.SET_NULL, null=True, blank=True)
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
    media = models.CharField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(unique=True)
    benefit = models.ForeignKey(Benefit, related_name='recipe_benefit', on_delete=models.SET_NULL, null=True, blank=True)
    store = models.ManyToManyField('Store', related_name='recipe_store')
    cook_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    ingredients = models.ManyToManyField('Ingredient', related_name='recipe_ingredient')
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

