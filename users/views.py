from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, UserChangeForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = '/skills/index.html'
    template_name = 'signup.html'

class UserChange(generic.CreateView):
    form_class = UserChangeForm
    success_url = '/skills/profile.html'
    template_name = 'edit_user.html'
