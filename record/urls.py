from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'record'
urlpatterns = [
    path('', views.main_view),
    path('reviews/', views.review_view, name='review'),
    path('write/', views.write_review,
         name='write_form'),
]
