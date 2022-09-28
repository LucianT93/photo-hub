from django.urls import path

from users import views

urlpatterns = [
    path('profile/<str:pk>', views.profile_view, name='profile')
]