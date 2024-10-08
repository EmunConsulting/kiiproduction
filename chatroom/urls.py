from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('rooms', views.rooms, name='rooms'),

    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<int:pk>/', views.update_room, name='update_room'),
    path('delete_room/<int:pk>/', views.delete_room, name='delete_room'),

    path('users_list', views.users_list, name='users_list'),
    path('<str:slug>', views.open_room, name='open_room'),
    path('send_message/<str:room_id>/', views.send_message, name='send_message'),
    path('start_private_chat/<int:user_id>/', views.start_private_chat, name='start_private_chat'),
    path('send_private_message/<int:chat_id>/', views.send_private_message, name='send_private_message'),
]