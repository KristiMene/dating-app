from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from myapp.models import Profile

#class ProfileForm(Profile):
#    class Meta:
#        model = User
#        fields = ('username', 'bio', 'gender','relationship status', 'looking for', 'education', 'birthdate' )
        
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)