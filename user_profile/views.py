from django.shortcuts import render


def dashboard(request):
    return render(request, 'user_profile/dashboard.html')
