from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'image',
            'meal_type',
            'ingredients',
            'instructions',
            'excerpt',
        ]
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 3}),
            'instructions': forms.Textarea(attrs={'rows': 10}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'meal_type': forms.CheckboxSelectMultiple(), 
        }
