from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select, Textarea, TextInput, PasswordInput, EmailInput

from photography.models import Rating
from users.models import Profile


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


class CreateProfileOnRegister(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
