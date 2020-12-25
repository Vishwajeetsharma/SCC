from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name="home_index"),
    path('handlerequest/', views.handleRequest, name="handle_request"),
    path('payments/', views.payments, name="payments"),
    # path('profile/', views.profile, name="profile"),
    # path('settings/', views.settings, name="settings"),
    # path('test/', views.test, name="test"),
    # path('result/', views.result, name="result"),
    # path('assignment/', views.assignment, name="assignment"),
    # path('studyMaterial/', views.studyMaterial, name="study-material"),
    # path('announcement/', views.announcement, name="announcement"),
    # path('password/', views.password, name="password"),
    path('class-11th/', views.c11th, name="c11th"),
    path('class-12th/', views.c12th, name="c12th"),
    path('B.Com-1st-year/', views.b1st, name="b1st"),
    path('B.Com-2nd-year/', views.b2nd, name="b2nd"),
    path('B.Com-3rd-year/', views.b3rd, name="b3rd"),
    path('add-class', views.add_in_a_class, name="add_in_a_class"),
]