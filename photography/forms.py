from django import forms
from django.contrib.auth.models import User
from django.forms import Select, Textarea, TextInput, PasswordInput

from photography.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value', 'body']

        widgets = {
            'value': Select(attrs={
                'class': 'form-select'
            }),
            'body': Textarea(attrs={
                'placeholder': 'Please enter your comment',
                'class': 'form-control',
                'rows': 3,
            })
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control'
            })
        }
