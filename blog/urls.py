from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('user_profile/<int:pk>', views.user_profile, name='user_profile'),
    path('user_profile_minimal/<int:pk>', views.user_profile_minimal, name='user_profile_minimal'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/<int:pk>/', views.update_profile, name='update_profile'),
    path('delete_profile/<int:pk>/', views.delete_profile, name='delete_profile'),

    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<int:pk>/', views.update_post, name='update_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),

    path('like_post/', views.like_post, name='like_post'),

    path('create_comment/<int:pk>', views.create_comment, name='create_comment'),
]

