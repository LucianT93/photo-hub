from django.urls import path

from users import views

urlpatterns = [
    path('profile/', views.profile_detail, name='profile'),
    path('update_profile/', views.update_profile, name='update-profile')
]