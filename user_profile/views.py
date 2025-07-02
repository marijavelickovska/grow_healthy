from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from recipe.models import Recipe


def dashboard(request):
    queryset = Recipe.objects.all()
    paginate_by = Paginator(queryset, 8)
    page_number = request.GET.get("page")
    recipes = paginate_by.get_page(page_number)

    context = {
        "recipes": recipes,
    }

    return render(
        request,
        "user_profile/dashboard.html",
        context,
    )


def my_recipes(request):
    return render(request, "user_profile/my_recipes.html")


def favourites(request):
    return render(request, "user_profile/favourites.html")


def add_recipe(request):
    return render(request, "user_profile/add_recipe.html")
