from django.urls import path

from users import views

urlpatterns = [
    path('profile/<str:pk>', views.ProfileDetail.as_view(), name='profile'),
    path('update_profile/<str:pk>', views.update_profile, name='update-profile')
]