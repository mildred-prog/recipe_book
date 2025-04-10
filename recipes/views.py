<<<<<<< HEAD
from django.views.generic import CreateView, ListView
=======
from django.views.generic import CreateView
>>>>>>> c4143b184631830becd95ccf91d2202f41e79ccf

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm

<<<<<<< HEAD

class Recipes(ListView):
    """View all recipes"""

    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)
=======
class AddRecipe(LoginRequiredMixin, CreateView):
    """ Add recipe view """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe).form_valid(form)
>>>>>>> c4143b184631830becd95ccf91d2202f41e79ccf
