from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request,'main.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        emailid = request.POST['emailid']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if not username or not username.isalpha():
            messages.success(request,'give an username only character ')
            return render(request,'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'signup.html')

        if not password or len(password) < 5:
            messages.success(request,'Password must be at least 8 characters long ')
            return render(request,'signup.html')

            

        # Add any additional fields as needed
        if password != confirmpassword:
             messages.success(request,'Password not match')
             return render(request,'signup.html')
        else:

        # Create a new user
            user = User.objects.create_user(username=username, password=password)
            # You may want to log in the user after signup
            login(request, user)
            return redirect('login')

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            # Handle invalid login
            pass

    return render(request, 'login.html')

def django(request):
    return render(request, 'django.html')

def express(request):
    return render(request, 'express.html')

def laravel(request):
    return render(request, 'laravel.html')

def spring(request):
    return render(request, 'springboot.html')

def ruby(request):
    return render(request, 'ruby.html')

def backend(request):
    return render(request, 'backend.html')

def frontend(request):
    return render(request, 'frontend.html')

def database(request):
    return render(request, 'database.html')

def react(request):
    return render(request, 'react.html')
    
def angular(request):
    return render(request, 'angular.html')

def next(request):
    return render(request, 'next.html')

def html(request):
    return render(request, 'html.html')

def vue(request):
    return render(request, 'vue.html')

def mongo(request):
    return render(request, 'mongodb.html')

def sql(request):
    return render(request, 'sql.html')

def psql(request):
    return render(request, 'psql.html')

def mariadb(request):
    return render(request, 'mariadb.html')

def redis(request):
    return render(request, 'redis.html')