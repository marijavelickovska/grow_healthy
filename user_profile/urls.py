from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_recipes/', views.dashboard, name='my_recipes'),
    path('favourites/', views.dashboard, name='favourites'),
    path('add_recipe/', views.dashboard, name='add_recipe'),
]
