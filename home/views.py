from django.shortcuts import render, redirect
from django.views import generic
from recipe.models import Recipe


class Home(generic.ListView):
    """
    Returns all recipes in :model:`recipe.Recipe`
    and displays them in a page of eight posts.
    **Context**

    ``queryset``
        All instances of :model:`recipe.Recipe`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`home/home.html`

    **Method override:**

    The `dispatch` method is overridden to check if the user is authenticated.
    If so, it redirects the user to the dashboard instead of showing the home page.
    Otherwise, it proceeds with the normal request dispatching process.
    """

    queryset = Recipe.objects.all()
    template_name = "home/home.html"
    paginate_by = 8
    context_object_name = 'recipe_list'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
