from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('fund_type_list/', views.fund_type_list, name='fund_type_list'),
    path('create_fund_type/', views.create_fund_type, name='create_fund_type'),
    path('update_fund_type/<int:pk>/', views.update_fund_type, name='update_fund_type'),
    path('delete_fund_type/<int:pk>/', views.delete_fund_type, name='delete_fund_type'),

    path('fund_record_list/', views.fund_record_list, name='fund_record_list'),
    path('fund_record_detail/<int:pk>', views.fund_record_detail, name='fund_record_detail'),
    path('create_fund_record/', views.create_fund_record, name='create_fund_record'),
    path('update_fund_record/<int:pk>/', views.update_fund_record, name='update_fund_record'),
    path('delete_fund_record/<int:pk>/', views.delete_fund_record, name='delete_fund_record'),

    path('investor_type_list/', views.investor_type_list, name='investor_type_list'),
    path('create_investor_type/', views.create_investor_type, name='create_investor_type'),
    path('update_investor_type/<int:pk>/', views.update_investor_type, name='update_investor_type'),
    path('delete_investor_type/<int:pk>/', views.delete_investor_type, name='delete_investor_type'),

    path('investor_record_list/', views.investor_record_list, name='investor_record_list'),
    path('create_investor_record/', views.create_investor_record, name='create_investor_record'),
    path('update_investor_record/<int:pk>/', views.update_investor_record, name='update_investor_record'),
    path('delete_investor_record/<int:pk>/', views.delete_investor_record, name='delete_investor_record'),
]
