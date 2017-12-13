from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_request, name='logout_request'),
    url(r'^login$', auth_views.login, name='login'),
    url(r'^posts$', views.posts, name='posts'),
    url(r'^$', views.index, name='index'),

    path('thread/<int:thread_id>', views.thread, name='thread'),
    path('posts/<int:post_id>/delete', views.delete_post, name='delete_post'),
]