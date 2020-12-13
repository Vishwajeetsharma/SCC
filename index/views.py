from django.shortcuts import render, redirect
from django.contrib import auth
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
            try:
                user = User.objects.get(email=email)
                return render(request, 'index/register.html', {'error': "Email Already Exist <a href='{% url 'login' %}'>Login</a>" })
            except User.DoesNotExist:
                user.objects.create_user(username=uname, email=email, password=pwd)
                auth.login(request, user)
                return redirect(request, 'index/login.html')
        else:
            return render(request, 'index/register.html', {'error': "Passwords Don't match", 'uname':uname, 'email':email,})
    else:
        return render(request, 'index/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']
        user = auth.authenticate(email=email, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect(reqest, 'index/register.html')
        else:
            return render(request, 'index/login.html', {'error':"Invalid Login Credentials",'email':email })
    else:
        return render(request, 'index/login.html')


def logout(request):
    auth.logout(request)
    return redirect(home)