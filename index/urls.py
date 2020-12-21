from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index_index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logoutbtn/', views.logoutbtn, name="logout"),
    path('forgot-password/', views.forgotPass, name="forgotPass")
]
