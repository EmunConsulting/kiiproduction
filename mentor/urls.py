from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('mentors_list/', views.mentors_list, name='mentors_list'),
    path('create_mentor/', views.create_mentor, name='create_mentor'),
    path('assign_mentor/<int:mentee>/<int:program>/', views.assign_mentor, name='assign_mentor'),
    path('show_mentor/<int:mentee>/<int:program>/', views.show_mentor, name='show_mentor'),
    path('update_mentor/<int:pk>/', views.update_mentor, name='update_mentor'),
    path('delete_mentor/<int:pk>/', views.delete_mentor, name='delete_mentor'),

    path('update_mentorship/<int:pk>/', views.update_mentorship, name='update_mentorship'),
    path('delete_mentorship/<int:pk>/', views.delete_mentorship, name='delete_mentorship'),

]
