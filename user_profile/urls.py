from django.urls import path
from recipe import views as recipe_views
from . import views


urlpatterns = [
    path("add_recipe/", recipe_views.add_recipe, name="add_recipe"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "favourites/",
        views.dashboard, {"filter_type": "favourites"}, name="favourites"
    ),
    path("my_recipes/",
         views.dashboard, {"filter_type": "my"}, name="my_recipes"),
    path("recipe/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/like/<int:pk>/", views.recipe_like, name="recipe_like"),
]
