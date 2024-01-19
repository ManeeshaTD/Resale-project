from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_username(self):
        return self.cleaned_data.get('username')

    def clean_password1(self):
        return self.cleaned_data.get('password1')


class SignUpForm(CustomUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].required = False



    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
class SignUpUpdateForm(CustomUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].required = False
        self.fields['password1'].required = False




    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['mobile' , 'image' , 'city' , 'state', 'address']

class LoginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username' , 'password' ]