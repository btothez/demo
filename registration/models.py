from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True)

class Category(models.Model):
	tag = models.CharField(max_length=50, blank=False)	

class Thread(models.Model):
    name = models.CharField(max_length=250, blank=False)	
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)	
    body = models.TextField(max_length=50000, blank=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
