from django.contrib import admin
from django.urls import path
from votingpage import views


urlpatterns = [
      
    path('',views.votingpage,name='votingpage'),
]