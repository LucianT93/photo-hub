from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select, Textarea, TextInput, PasswordInput, EmailInput

from photography.models import Photography, Comment
from users.models import Profile


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
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
