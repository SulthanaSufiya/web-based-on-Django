from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request,'index.html')

def signup_view(request):
   return render(request,'signup.html')

def forgot_password_view(request):
    return render(request, 'forgotpassword.html')

def login_view(request):
   return render(request,'login.html')

