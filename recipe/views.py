from django.shortcuts import render
from .models import Recipe, Category
from recipe import views 

def recipe(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/main.html', {'recipes': recipes})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipe/category_list.html', {'categories': categories})

def homepage(request):
    recipes = Recipe.objects.all()
    return render(request, 'base.html', {'recipes': recipes})
