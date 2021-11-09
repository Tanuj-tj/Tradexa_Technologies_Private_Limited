from django.contrib import admin
from django.urls import path, include
from django.http.response import HttpResponse
from . import views


urlpatterns = [
    path('create_Post/', views.createPost, name='create_Post' ),
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('success/', views.successPage, name='success_Page' ),
]
 