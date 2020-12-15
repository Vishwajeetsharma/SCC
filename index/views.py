from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from oauth2client.contrib.django_util.models import CredentialsField

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
            return HttpResponse("Success")
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