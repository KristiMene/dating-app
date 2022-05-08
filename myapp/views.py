from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
def dashboard(request):
    return render(request, "base.html")


@login_required
def profile_list(request):
    my_profile = request.user.profile
    profiles = Profile.objects.exclude(user=request.user).all()
    if my_profile.looking_for != Profile.BOTH:
        profiles = profiles.filter(gender=my_profile.looking_for)
    return render(request, "myapp/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    # print(profile)
    return render(request, "myapp/profile.html", {"profile": profile})


class AdminLogin(LoginView):
    template_name = "login.html"


def home(request):
    return render(request, "home.html")
