from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('program_category_list/', views.program_category_list, name='program_category_list'),
    path('create_program_category/', views.create_program_category, name='create_program_category'),
    path('update_program_category/<int:pk>/', views.update_program_category, name='update_program_category'),
    path('delete_program_category/<int:pk>/', views.delete_program_category, name='delete_program_category'),

    path('program_list/', views.program_list, name='program_list'),
    path('events_list/', views.events_list, name='events_list'),
    path('current_events_list/', views.current_events_list, name='current_events_list'),
    path('create_program_list/', views.create_program_list, name='create_program_list'),
    path('update_program_list/<int:pk>/', views.update_program_list, name='update_program_list'),
    path('delete_program_list/<int:pk>/', views.delete_program_list, name='delete_program_list'),

    path('planned_program_list/', views.planned_program_list, name='planned_program_list'),
    path('approved_attendees_list/<int:pk>/', views.approved_attendees_list, name='approved_attendees_list'),
    path('create_program/', views.create_program, name='create_program'),
    path('update_program/<int:pk>/', views.update_program, name='update_program'),
    path('delete_program/<int:pk>/', views.delete_program, name='delete_program'),
]
