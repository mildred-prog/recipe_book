from django.urls import path
<<<<<<< HEAD
from .views import (
    AddRecipe, Recipes,
    # RecipeDetail, DeleteRecipe,
    # EditRecipe
)


urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", Recipes.as_view(), name="recipes"),
=======
from .views import AddRecipe

urlpatterns = [
    path('', AddRecipe.as_view(), name='add_recipe'),
>>>>>>> c4143b184631830becd95ccf91d2202f41e79ccf
]