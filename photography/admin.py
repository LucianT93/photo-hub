from django.contrib import admin

# Register your models here.

from .models import Photography, Category, RatingLikeDislike, Comment

admin.site.register(Photography)
admin.site.register(RatingLikeDislike)
admin.site.register(Comment)
admin.site.register(Category)

