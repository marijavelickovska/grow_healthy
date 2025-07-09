from .models import Profile
from .forms import ProfileForm


def get_profile_context(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    profile_form = ProfileForm(instance=profile)
    return profile, profile_form
