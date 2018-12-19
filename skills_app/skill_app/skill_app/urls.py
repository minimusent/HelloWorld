from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('skills/', include('skills.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
