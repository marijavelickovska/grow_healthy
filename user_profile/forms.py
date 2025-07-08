from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'about']
        labels = {
            'image': '',
            'name': 'Your name',
            'about': 'Something about you',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control profile-fields',
                'id': 'nameInput',
                'disabled': True
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control profile-fields',
                'id': 'aboutInput',
                'rows': 3,
                'disabled': True
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control d-none',
                'id': 'profileImgInput',
                'accept': 'image/*'
            })
        }
