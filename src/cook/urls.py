from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import utils, views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'stores', views.StoreViewSet)
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'recipes', views.RecipeViewSet)
router.register(r'recipe_ingredients', views.RecipeIngredientViewSet)
schema_view = get_schema_view(title='Don\'t Starve Crockpot API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    
    url(r'^upload-stores/(?P<filename>[^/]+)$',
        utils.UploadStoresView.as_view(),
        name='upload-stores-csv'),
    
    url(r'^upload-categories/(?P<filename>[^/]+)$',
        utils.UploadCategoriesView.as_view(),
        name='upload-categories-csv'),
]