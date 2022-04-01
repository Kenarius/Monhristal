from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'record'
urlpatterns = [
    path('', views.main_view),
    path('reviews/', views.review_view, name='review'),
    path('write/', views.write_review,
         name='write_form'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myrecords/', views.records_view, name='myrecords'),
    path('record/', views.make_record, name='record'),
]
