from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Meal model.
    Displays meal info and allows search and filtering.
    """
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)