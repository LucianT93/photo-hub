from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select, Textarea, TextInput, PasswordInput, EmailInput

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
                'class': 'form-control',
                'id': 'username_login'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password_login'
            })
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your username'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your username'
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your password'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your confirmation password'
            }
        )
