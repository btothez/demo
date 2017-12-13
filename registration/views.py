from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.shortcuts import render, redirect
from .forms import RegistrationForm, PostForm
from .models import Post, Thread, Category
from .services import add_new_post
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.template import loader

import sys

def logout_request(request):
    user = request.user
    logout(request)
    return redirect('register')

def login_request(request):
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    user = request.user
    full_name = ''
    if not user.is_authenticated:
        return redirect('register')
    full_name = "{} {}".format(user.first_name, user.last_name)
    full_name = full_name.title()
    return render(request, 'registration/index.html', {'user': user, 
                                                       'full_name': full_name})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def posts(request):
    if request.method == 'POST':
        data = request.POST

        title = data['title']
        body = data['body']
        thread = data['thread']
        new_thread = data['new_thread']
        category = data['category']
        new_category = data['new_category']
        body = data['body']

        if not category:
            cat = Category(tag=new_category)
            cat.save()
        else:
            cat = Category.objects.get(id=category)

        print()
        print('category')
        print(cat)

        if not thread:
            thr = Thread(name=new_thread, category=cat)
            thr.save()
        else:
            thr = Thread.objects.get(id=thread)

        print()
        print('Thread')
        print(thr)

        pst = Post(title=title, body=body, thread=thr)
        pst.save()
        pst.user.add(request.user)

        return redirect('index')
    else:
        form = PostForm()
        threads = Thread.objects.all()
        categories = Category.objects.all()
        context = {
            'form': form,
            'threads': threads,
            'categories': categories
        }
        return render(request, 'registration/posts.html', context)