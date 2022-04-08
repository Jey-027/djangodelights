from time import timezone
from django.db import models

# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()

    def get_absolute_url(self):
        pass

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    title = models.CharField(max_length= 40)
    price = models.FloatField()

    def __str__(self) :
        return f"{self.title}"

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self) :
        return f"{self.menu_item}"

class purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item}"