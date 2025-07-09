from .models import Profile
from .forms import ProfileForm


def profile_context(request):
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        return {
            "profile": profile,
            "profile_form": profile_form
        }
    return {}
