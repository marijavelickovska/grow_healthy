from django.shortcuts import render


def dashboard(request):
    return render(request, 'user_profile/dashboard.html')


def my_recipes(request):
    return render(request, 'user_profile/my_recipes.html')


def favourites(request):
    return render(request, 'user_profile/favourites.html')


def add_recipe(request):
    return render(request, 'user_profile/add_recipe.html')
