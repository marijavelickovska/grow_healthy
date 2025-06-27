from django.contrib import admin
from .models import Profile


admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.
    Displays user info and allows search and filtering.
    """

    list_display = ('user', 'name', 'created_on')
    search_fields = ['user', 'name']
    list_filter = ('created_on',)