from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name="index_index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logoutbtn/', views.logoutbtn, name="logout"),
    
    # reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="index/forgotPass.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="index/sentPass.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="index/changePass.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="index/completePass.html"), name="password_reset_complete"),
]
