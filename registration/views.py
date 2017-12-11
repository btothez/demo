from django.contrib.auth import login, authenticate, logout
from django.db import transaction

from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.http import HttpResponse
from django.template import loader

import sys

def logout_request(request):
    user = request.user
    logout(request)
    return redirect('register')

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