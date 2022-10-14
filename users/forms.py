from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

from users.models import Profile, Camera, Lens


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
                'placeholder': 'Please enter your username',
                'id': 'username_register'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your username',
                'id': 'email_register'
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your password',
                'id': 'pass1_register'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Please enter your confirmation password',
                'id': 'pass2_register'
            }
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'profile_image', 'social_instagram', 'social_youtube', 'social_forum',
                  'social_facebook', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'id': 'profile_description',
                'rows': '3'
            }
        )
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                    'id': f'{field}'
                }
            )


class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'id': 'camera_description'
            }),
        }


class LensForm(forms.ModelForm):
    class Meta:
        model = Lens
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'id': 'lens_description'
            }),
        }
