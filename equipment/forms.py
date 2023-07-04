from django import forms
from django.forms import TextInput, Select

from equipment.models import Camera, Lens


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
        fields = ['camera']

        widgets = {
            'camera': Select(attrs={
                'class': 'form-control',
                'id': 'lens_description'
            }),
        }