from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name=''),
    path('register',views.register_user,name='register'),

        ]