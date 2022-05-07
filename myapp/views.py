from re import template
from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.forms import modelformset_factory
from myapp.forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Profile
from django.contrib.auth.views import LoginView    



# Create your views here.
def dashboard(request):
    return render(request, 'base.html')

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'myapp/profile_list.html', {'profiles':profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    #print(profile)
    return render(request, 'myapp/profile.html', {'profile':profile})

class AdminLogin(LoginView):
    template_name = "login.html"
    
def home(request):
    return render(request, 'home.html')
    
    
    
