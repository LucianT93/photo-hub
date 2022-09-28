from django.contrib import admin

from .models import Profile, Camera, Lens

# Register your models here.

admin.site.register(Profile)
admin.site.register(Camera)
admin.site.register(Lens)
