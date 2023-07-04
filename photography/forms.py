from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select, Textarea, TextInput, PasswordInput, EmailInput, ImageField

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


class CreatePostPhoto(forms.ModelForm):
    class Meta:
        model = Photography
        fields = ['title', 'description', 'image', 'category']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Please enter the title of the post',
                'class': 'form-control'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Enter a description here',
                'class': 'form-control',
                'rows': 2
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control',
                'id': 'formFile'
            }
        )
        self.fields['category'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
