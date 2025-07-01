from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('favourites/', views.favourites, name='favourites'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]
