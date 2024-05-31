from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            ingredients='Test Ingredients',
            category=self.category
        )


    def test_recipe_view(self):
        response = self.client.get(reverse('recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/category_list.html')
