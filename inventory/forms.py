from dataclasses import field
from pyexpat import model
from django import forms
from .models import Ingredients, RecipeRequirements, MenuItem, purchase


class ingredients_form(forms.Form):
    class Meta:
        model = Ingredients
        field = "__all__"
        