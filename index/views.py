from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index_index')
    if request.method == "POST":
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        pwdCon = request.POST['passwordConf']
        if User.objects.filter(username=uname).exists():
            return render(request, 'index/register.html', {'error': "Username already exists.", 'email':email,})
        if User.objects.filter(email=email).exists():
            return render(request, 'index/register.html', {'error': "Email already exists.", 'uname':uname})
        if len(uname) < 1:
            return render(request, 'index/register.html', {'error': "Empty feilds are not allowed", 'uname':uname, 'email':email,})
        if len(email) < 1:
            return render(request, 'index/register.html', {'error': "Empty feilds are not allowed", 'uname':uname, 'email':email,})
        if not uname.isalnum:
            return render(request, 'index/register.html', {'error': "Username can only contain numbers and letters", 'uname':uname, 'email':email,})
        if pwd != pwdCon:
            return render(request, 'index/register.html', {'error': "Passwords Don't match", 'uname':uname, 'email':email,})
        if len(pwd) < 6:
            return render(request, 'index/register.html', {'error': "Passwords should not less than 6", 'uname':uname, 'email':email,})
        else:
            user = User.objects.create_user(uname, email, pwd)
            auth_login(request, user)
            template = render_to_string('index/email_conf.html', {'name': uname})
            email = EmailMessage(
                'Thank you for joing SCC - Shukla Commerce Classes',
                template,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return redirect('index_index')
    else:
        return render(request, 'index/register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('index_index')
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

def agasdf(request):
    if request.method == 'POST':
        return render(request, 'index/forgotPass.html', { 'alert':"alert-success", 'error': "Password reset link successfully sent on yor email" })
    else:
        return render(request, 'index/forgotPass.html')