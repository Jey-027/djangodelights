from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('ingredient/list', views.ingredients_list.as_view(), name="Inventory_ingredients"),
]