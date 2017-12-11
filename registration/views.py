from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from .forms import RegistrationForm, 
from .forms import UserForm, ProfileForm

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Profile


import sys
def index(request):
    pass
	# context = {
	# 	'something': 'else'
	# }
	# template = loader.get_template('registration/index.html')
	# return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            email = user_form.cleaned_data.get('email')
            raw_password = user_form.cleaned_data.get('password')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            print(list(user_form.errors.keys()))
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'registration/register.html', {'user_form': user_form, 
                                                          'profile_form': profile_form})

'''
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })'''
