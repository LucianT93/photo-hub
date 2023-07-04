from django.urls import path

from photography import views

urlpatterns = [
    path('', views.photo_post_home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('rating_form/', views.comment_form, name='rating_form'),
    # path('like_dislike/', views.like_dislike_rating, name='like_dislike'),
    # path('like_owners/<str:pk>', views.get_like_owners, name='like_owners')
    path('create_post/', views.create_post, name='create_post')
]
