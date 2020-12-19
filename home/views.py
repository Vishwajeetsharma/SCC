from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.views import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def home_index(request):
    return render(request, 'home/index.html')

@login_required(login_url="/login/")
def profile(request):
    return HttpResponse(" profile ")

@login_required(login_url="/login/")
def settings(request):
    return HttpResponse(" settings ")

@login_required(login_url="/login/")
def test(request):
    return HttpResponse(" test ")

@login_required(login_url="/login/")
def result(request):
    return HttpResponse(" result ")

@login_required(login_url="/login/")
def assignment(request):
    return HttpResponse(" assignment ")

@login_required(login_url="/login/")
def studyMaterial(request):
    return HttpResponse(" study-material ")

@login_required(login_url="/login/")
def announcement(request):
    return HttpResponse(" announcement ")

@login_required(login_url="/login/")
def password(request):
    return render(request, 'home/content/password.html')

@login_required(login_url="/login/")
def password(request):
    return render(request, 'home/content/password.html')