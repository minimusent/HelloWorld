from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.home, name='home'),
    url(r'^profile', views.profile, name='profile'),
	url(r'^summary', views.summary, name='summary'),
    url(r'^new_job/$', views.job_new, name='new_job'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^candidates', views.candidates, name='candidates'),
    url(r'^search/', views.search, name='search'),
    #url(r'^requirement-autocomplete/$', RequirementAutocomplete.as_view(), name='requirement-autocomplete',),
]
