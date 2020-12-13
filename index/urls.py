from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]
