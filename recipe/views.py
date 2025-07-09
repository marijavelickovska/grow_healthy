from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Recipe
from .forms import RecipeForm


@login_required
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
            messages.error(
                request,
                "There was an error in your submission. Please check the form."
                )
    else:
        recipe_form = RecipeForm()

    context = {
        "recipe_form": recipe_form,
        'is_edit': False,
    }

    return render(
        request,
        'user_profile/add_recipe.html',
        context,
    )


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.author != request.user:
        messages.error(request, "You are not allowed to edit this recipe.")
        return HttpResponseForbidden(
            "You are not allowed to edit this recipe.")

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('recipe_detail', pk=recipe.id)
        else:
            messages.error(request, "There was an error updating the recipe. Please check the form.")
    else:
        recipe_form = RecipeForm(instance=recipe)

    context = {
        "recipe_form": recipe_form,
        'is_edit': True
    }

    return render(
        request,
        'user_profile/add_recipe.html',
        context
        )


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.author == request.user:
        recipe.delete()
        messages.success(request, "Recipe successfully deleted!")
        return redirect("my_recipes")
    else:
        messages.warning(request, "You must confirm deletion.")
        return redirect("recipe_detail", pk=recipe.id)
