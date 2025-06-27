from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meal, Recipe


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Meal model.
    Displays meal info and allows search and filtering.
    """
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Recipe model.
    Displays recipe info, allows search and filtering,
    prepopulated fields and rich-text editor.
    """

    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'author__username']
    list_filter = ('meal_type', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')
