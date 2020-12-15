from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name="home_index"),
    path('profile/', views.profile, name="profile"),
    path('settings/', views.settings, name="settings"),
    path('test/', views.test, name="test"),
    path('result/', views.result, name="result"),
    path('assignment/', views.assignment, name="assignment"),
    path('studyMaterial/', views.studyMaterial, name="study-material"),
    path('announcement/', views.announcement, name="announcement"),
    path('password/', views.password, name="password")
]