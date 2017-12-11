from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_request, name='logout_request'),
    url(r'^$', views.index, name='index'),
]