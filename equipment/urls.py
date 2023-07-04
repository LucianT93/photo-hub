from django.urls import path

from equipment import views

urlpatterns = [
    path('camera/', views.get_camera, name='camera'),
    path('lens/', views.get_lens, name='lens'),
]
