from django.contrib import admin
from django.urls import path
from result import views


urlpatterns = [
      
    path('',views.result,name='result'),
]