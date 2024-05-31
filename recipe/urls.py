from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
    path('categories/', views.category_list, name='category_list'),
]


