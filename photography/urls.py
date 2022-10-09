from django.urls import path

from photography import views

urlpatterns = [
    path('', views.PhotoPostHome.as_view(), name='home'),
    path('logout/', views.logoutUser, name='logout'),
]
