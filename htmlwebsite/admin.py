from django.contrib import admin
from htmlwebsite.models import Contact,studentlogin,newuser,adminelogin

# Register your models here.

admin.site.register(Contact)
admin.site.register(studentlogin)
admin.site.register(newuser)
admin.site.register(adminelogin)

