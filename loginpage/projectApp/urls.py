from django.contrib import admin
from django.urls import path
from projectApp import views




urlpatterns = [
    path('',views.login,name='login'),
    path('next',views.namepage,name='namepage')
   
]
