from django.contrib import admin

# Register your models here.

from .models import Photography, Rating, Category

admin.site.register(Photography)
admin.site.register(Rating)
admin.site.register(Category)