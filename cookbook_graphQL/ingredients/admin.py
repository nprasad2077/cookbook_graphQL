from django.contrib import admin
from cookbook_graphQL.ingredients.models import Category, Ingredient

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredient)