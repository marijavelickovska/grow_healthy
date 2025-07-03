from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RecipeForm


def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            recipe_form.save_m2m()
            messages.success(request, "Recipe added successfully.")
            return redirect('my_recipes')
    else:
        recipe_form = RecipeForm()

    context = {
        "recipe_form": recipe_form,
    }

    return render(
        request,
        'user_profile/add_recipe.html',
        context,
    )
