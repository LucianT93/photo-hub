from django.urls import path

from users import views

urlpatterns = [
    path('profile/', views.profile_detail, name='profile'),
]