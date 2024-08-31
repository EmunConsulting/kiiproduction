from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('service_products_list/', views.service_products_list, name='service_products_list'),
    path('create_service_products/', views.create_service_products, name='create_service_products'),
    path('update_service_products/<int:pk>/', views.update_service_products, name='update_service_products'),
    path('delete_service_products/<int:pk>/', views.delete_service_products, name='delete_service_products'),

    path('registration_status_list/', views.registration_status_list, name='registration_status_list'),
    path('create_registration_status/', views.create_registration_status, name='create_registration_status'),
    path('update_registration_status/<int:pk>/', views.update_registration_status, name='update_registration_status'),
    path('delete_registration_status/<int:pk>/', views.delete_registration_status, name='delete_registration_status'),

    path('development_stage_list/', views.development_stage_list, name='development_stage_list'),
    path('create_development_stage/', views.create_development_stage, name='create_development_stage'),
    path('update_development_stage/<int:pk>/', views.update_development_stage, name='update_development_stage'),
    path('delete_development_stage/<int:pk>/', views.delete_development_stage, name='delete_development_stage'),

    path('industry_sector_list/', views.industry_sector_list, name='industry_sector_list'),
    path('create_industry_sector/', views.create_industry_sector, name='create_industry_sector'),
    path('update_industry_sector/<int:pk>/', views.update_industry_sector, name='update_industry_sector'),
    path('delete_industry_sector/<int:pk>/', views.delete_industry_sector, name='delete_industry_sector'),

    path('business_list/', views.business_list, name='business_list'),
    path('create_business/', views.create_business, name='create_business'),
    path('update_business/<int:pk>/', views.update_business, name='update_business'),
    path('delete_business/<int:pk>/', views.delete_business, name='delete_business'),

    path('outcome_record_list/<int:pk>/', views.outcome_record_list, name='outcome_record_list'),
    path('create_outcome_record/<int:pk>/', views.create_outcome_record, name='create_outcome_record'),
    path('update_outcome_record/<int:pk>/', views.update_outcome_record, name='update_outcome_record'),
    path('delete_outcome_record/<int:pk>/', views.delete_outcome_record, name='delete_outcome_record'),

]
