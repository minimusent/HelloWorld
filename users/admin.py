from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, UserChangeForm
from .models import User

#class CustomUserAdmin(UserAdmin):
#    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm
#    model = User
#    list_display = ['email', 'username', 'first_name', 'last_name', 'summary', 'min_salary', 'get_skills',]

#admin.site.register(User, CustomUserAdmin)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('summary', 'min_salary', 'skills',)}),
    )

admin.site.register(User, MyUserAdmin)
