from django.urls import path
from recipe import views as recipe_views
from . import views


urlpatterns = [
    path("add_recipe/", recipe_views.add_recipe, name="add_recipe"),
    path("edit_recipe/<int:recipe_id>/",
         recipe_views.edit_recipe, name="edit_recipe"),
    path("delete_recipe/<int:recipe_id>/",
         recipe_views.delete_recipe, name='delete_recipe'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "favourite/",
        views.dashboard, {"filter_type": "favourites"}, name="favourites"
    ),
    path(
        "favourite_add/<int:recipe_id>",
        views.add_to_favourites, name="add_to_favourites"
    ),
    path(
        "favourite_remove/<int:recipe_id>",
        views.remove_from_favourites, name="remove_from_favourites"
    ),
    path("my_recipes/",
         views.dashboard, {"filter_type": "my"}, name="my_recipes"),
    path("recipe/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/like/<int:pk>/", views.recipe_like, name="recipe_like"),
    path("recipe/unlike/<int:pk>/", views.recipe_unlike, name="recipe_unlike"),
    path("recipe/<int:recipe_id>/edit_comment/<int:comment_id>/",
         views.comment_edit, name="comment_edit"),
    path('recipe/<int:recipe_id>/delete_comment/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),
]
