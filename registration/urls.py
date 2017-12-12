from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_request, name='logout_request'),
    url(r'^login$', auth_views.login, name='login'),
    url(r'^$', views.index, name='index'),
]