from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# class UserForm(UserCreationForm):
#     # first_name = forms.CharField(max_length=30, required=True)
#     # last_name = forms.CharField(max_length=30, required=True)
#     # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     # bio = forms.CharField(widget=forms.Textarea())

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'bio')

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)