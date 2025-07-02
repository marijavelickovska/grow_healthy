from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_recipes/', views.dashboard, {'filter_type': 'my'}, name='my_recipes'),
    path('favourites/', views.dashboard, {'filter_type': 'favourites'}, name='favourites'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]
