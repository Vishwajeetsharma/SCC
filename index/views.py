from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        pwdCon = request.POST['passwordConf']
        if pwd == pwdCon:
            User.objects.create_user(uname, email, pwd)
            return render(request, '/login')
        else:
            return render(request, 'index/register.html', {'error': "Passwords Don't match", 'uname':uname, 'email':email,})
    else:
        return render(request, 'index/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index_index')
        else:
            return render(request, 'index/login.html', {'error':"Invalid Login Credentials",'username':username })
    else:
        return render(request, 'index/login.html')


def logoutbtn(request):
    logout(request)
    return redirect('index_index')