from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Ingredients
# Create your views here.


def home(request):
    return render(request, 'inventory/home.html')


class ingredients_list(ListView):
    model = Ingredients
    context_object_name = "ingredients_list"






