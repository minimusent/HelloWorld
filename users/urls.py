from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # login Page
    # url('r^login/$', auth_views.login, name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit_user/', views.UserChange.as_view(), name='edit_user'),
]
