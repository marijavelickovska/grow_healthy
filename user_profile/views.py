from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from recipe.models import Recipe


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


def add_recipe(request):
    return render(request, "user_profile/add_recipe.html")
