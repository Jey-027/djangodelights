from tkinter import Menu
from django.contrib import admin
from .models import Ingredients, MenuItem, RecipeRequirements, purchase

# Register your models here.

admin.site.register(Ingredients)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirements)
admin.site.register(purchase)

