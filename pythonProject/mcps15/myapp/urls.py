from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.loginview,name='login'),
    path('register',views.registrationview,name='register'),
    path('home',views.homeview,name='home')

]
