from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title", "description", "ingredients", "instructions",
            "image", "image_alt", "meal_type", "cuisine_type", "calories"
        ]
