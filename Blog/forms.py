from django import forms
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog, Subscribers
from pagedown.widgets import AdminPagedownWidget


class ProfileAuthenticationForm(AuthenticationForm):
    username = UsernameField(label='',
                             required=True, max_length=200,
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Username', 'spellcheck': 'false', 'autofocus': False}))
    password = forms.CharField(
        label='',
        strip=False,
        required=True, max_length=200,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'autocomplete': 'current-password',
                'spellcheck': 'false',
                'type': 'password'}),
    )

    class Meta:
        model = User


class NewBlogForm(forms.ModelForm):
    Title = forms.CharField(
        strip=False,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': "Article Title",
            'type': 'text',
        }))

    slug = forms.CharField(
        strip=False,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': "Article Slug",
            'type': 'text',
        }))

    class Meta:
        model = Blog
        fields = ('Title', 'Author', 'slug', 'created_at', 'Body',)


class SubForm(forms.ModelForm):
    Email = forms.CharField(
        label='',
        strip=False,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': "Email",
            'type': 'email',
        }))

    class Meta:
        model = Subscribers
        fields = ['Email']
