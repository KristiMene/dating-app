from django.urls import path
from .views import dashboard, profile_list, profile, dashboard, AdminLogin, home
app_name = "myapp"

urlpatterns = [
    path("", dashboard, name='dashboard'),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("login/", AdminLogin.as_view(), name='login'),
    path("home/", home, name="home")
    
]
