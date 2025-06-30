from django.shortcuts import render


# Create your views here.
def my_recipes(request):
    return render(request, 'recipe/my_recipes.html')
