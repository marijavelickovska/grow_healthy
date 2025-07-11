from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Form class for users to store profile information.
    """
    class Meta:
        model = Profile
        fields = ['image', 'name', 'about']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control profile-fields',
                'id': 'nameInput',
                'placeholder': 'Your name',
                'disabled': True
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control profile-fields',
                'id': 'aboutInput',
                'rows': 3,
                'placeholder': 'Something about you',
                'disabled': True
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control d-none',
                'id': 'profileImgInput',
                'accept': 'image/*'
            })
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['about'].label = ""
