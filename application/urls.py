from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('application_list/', views.application_list, name='application_list'),
    path('pending_application_list/', views.pending_application_list, name='pending_application_list'),
    path('create_application/<int:pk>/', views.create_application, name='create_application'),
    path('approve_application/<int:pk>/', views.approve_application, name='approve_application'),
    path('update_application/<int:pk>/', views.update_application, name='update_application'),
    path('delete_application/<int:pk>/', views.delete_application, name='delete_application'),
    path('delete_application_user/<int:pk>/', views.delete_application_user, name='delete_application_user'),

]
