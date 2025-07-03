from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from recipe.models import Recipe, Like


def dashboard(request, filter_type=None):
    user = request.user

    if filter_type == 'my':
        queryset = Recipe.objects.filter(author=user)
    elif filter_type == 'favourites':
        # претпоставувам имаш поврзана релација favourites
        queryset = Recipe.objects.filter(favourited_by__user=user)
    else:
        queryset = Recipe.objects.all()

    paginate_by = Paginator(queryset, 8)
    page_number = request.GET.get("page")
    recipes = paginate_by.get_page(page_number)

    context = {
        "recipes": recipes,
        'filter_type': filter_type,
    }

    return render(
        request,
        "user_profile/dashboard.html",
        context,
    )


def recipe_detail(request, pk):
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, pk=pk)

    context = {
        "recipe": recipe,
    }

    return render(
        request,
        "user_profile/recipe_detail.html",
        context,
    )


@login_required
def recipe_like(request, pk):
    user = request.user
    recipe = get_object_or_404(Recipe, id=pk)

    # add record to Like model
    try:
        Like.objects.create(user=user, recipe=recipe)
        messages.success(request, f"You liked {recipe.title}!")
    except IntegrityError:
        messages.warning(request, f"You've already liked {recipe.title}!")
        pass

    # Redirects user back to previous page if referer exists, else to dashboard
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect('dashboard')
