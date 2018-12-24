from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.home, name='home'),
    url(r'^profile', views.profile, name='profile'),
	url(r'^summary', views.summary, name='summary'),
    url(r'^add_job', views.add_job, name='add_job'),
   # url(r'^edit_job', views.edit_job, name='edit_job'),
    url(r'^delete/(?P<skill_id>[0-9]+)/$', views.delete_skill, name='delete_skill'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^candidates', views.candidates, name='candidates'),
    url(r'^search/', views.search, name='search'),
    #url(r'^requirement-autocomplete/$', RequirementAutocomplete.as_view(), name='requirement-autocomplete',),
]
