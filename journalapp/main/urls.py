
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('panel/', views.panel, name='panel'),
    re_path(r'signup/', views.signup, name='signup'),
    re_path(r'login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),


]
