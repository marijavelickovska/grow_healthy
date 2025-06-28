from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meal, Recipe, Favourite, Like, Comment


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


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Favourite model.
    Displays favourite info and allows search and filtering.
    """
    list_display = ('user', 'recipe', 'added_at')
    search_fields = ['user__username', 'recipe__title']
    list_filter = ('added_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Like model.
    Displays like info and allows search and filtering.
    """
    list_display = ('user', 'recipe', 'created_on')
    search_fields = ['user__username', 'recipe__title']
    list_filter = ('created_on',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.
    Displays comment info, allows search and filtering.
    """
    list_display = ('recipe', 'author', 'created_on')
    search_fields = ['body', 'author__username', 'recipe__title']
    list_filter = ('created_on',)
