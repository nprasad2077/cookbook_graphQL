import graphene
from graphene_django import DjangoObjectType  

from cookbook_graphQL.ingredients.models import Ingredient, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes",  "category")

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    
    def resolve_all_ingredients(root, info):
        
        return Ingredient.objects.select_related("category").all()
    
    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except:
            return None
        
schema = graphene.Schema(query=Query)

# this is like the top URLs.py 