from django.urls import path

from photography import views

urlpatterns = [
    path('', views.photo_posts, name='home')
]
