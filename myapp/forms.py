from django import forms


# class ProfileForm(Profile):
#    class Meta:
#        model = User
#        fields = ('username', 'bio', 'gender','relationship status',
#                  'looking for', 'education', 'birthdate' )


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
