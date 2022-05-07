from .models import Profile
from django.shortcuts import render
from django.contrib.auth.views import LoginView


# Create your views here.
def dashboard(request):
    return render(request, "base.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "myapp/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    # print(profile)
    return render(request, "myapp/profile.html", {"profile": profile})


class AdminLogin(LoginView):
    template_name = "login.html"


def home(request):
    return render(request, "home.html")
