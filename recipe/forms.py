from django import forms
from .models import Recipe, Comment


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


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a recipe
    """
    class Meta:
        """
        Specify the django model and the fields
        """
        model = Comment
        fields = ['body']
        labels = {
            'body': '',  
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            }),
        }