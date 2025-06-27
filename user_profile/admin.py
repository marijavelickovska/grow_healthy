from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.
    Displays user info and allows search and filtering.
    """

    list_display = ('user', 'name', 'created_on')
    search_fields = ['user', 'name']
    list_filter = ('created_on',)