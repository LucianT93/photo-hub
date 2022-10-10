from django.urls import path

from photography import views

urlpatterns = [
    path('', views.PhotoPostHome.as_view(), name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('rating_form/', views.rating_form, name='rating_form')
]
