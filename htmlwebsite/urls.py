from django.contrib import admin
from django.urls import include,path
from htmlwebsite import views

app_name = 'htmlwebsite'

urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('forgotpassword/', views.forgot_password_view, name='forgotpassword'),
   path('login/',views.login_view,name='login'),
    
]

