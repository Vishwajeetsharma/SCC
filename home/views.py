from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.views import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def home_index(request):
    if request.user.groups.exists():
        ls = request.user.groups.all()[0].name
        if ls == 'c11th':
            return redirect('c11th')
        if ls == 'c12th':
            return redirect('c12th')
        if ls == 'b1st':
            return redirect('b1st')
        if ls == 'b2nd':
            return redirect('b2nd')
        if ls == 'b3rd':
            return redirect('b3rd')
    return render(request, 'home/index.html')

@login_required(login_url="/login/")
def c11th(request):
    ls = request.user.groups.all()[0].name
    if ls == 'c11th':
        return HttpResponse('class11')
    else:
        return redirect('home_index')
    
@login_required(login_url="/login/")
def c12th(request):
    ls = request.user.groups.all()[0].name
    if ls == 'c12th':
        return HttpResponse('class12')
    else:
        return redirect('home_index')

@login_required(login_url="/login/")
def b1st(request):
    ls = request.user.groups.all()[0].name
    if ls == 'b1st':
        return HttpResponse('B.Com 1st year')
    else:
        return redirect('home_index')

@login_required(login_url="/login/")
def b2nd(request):
    ls = request.user.groups.all()[0].name
    if ls == 'b2nd':
        return HttpResponse('B.Com 2nd year')
    else:
        return redirect('home_index')

@login_required(login_url="/login/")
def b3rd(request):
    ls = request.user.groups.all()[0].name
    if ls == 'b3rd':
        return HttpResponse('B.Com 3rd year')
    else:
        return redirect('home_index')