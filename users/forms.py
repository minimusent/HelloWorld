from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['username',
                    'email',
                    'first_name',
                    'last_name',
                    'city',
                    'state',
                    'summary',
                    'min_salary',
                    'skills',]

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        exclude = ('password',)
        fields = [
                    'email',
                    'first_name',
                    'last_name',
                    'city',
                    'state',
                    'summary',
                    'min_salary',
                    'skills',]

#class CustomUserChangeForm(UserChangeForm):

#    class Meta:
#        model = User
#        fields = ('username', 'email')
