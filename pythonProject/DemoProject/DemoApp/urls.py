from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homefun,name=''),
    path('home',views.homefun,name='home'),
    path('login',views.loginfun, name='login'),
    path('register',views.regfun,name='register'),
    path('aboutus',views.aboutusfun,name='aboutus'),
    path('adminreg',views.adminfun,name='adminreg'),
    path('show/', views.show_users, name='show-users'),
    path('edit/<int:pk>', views.edit_user, name='edit-user'),
    path('delete/<int:pk>', views.delete_user, name='delete-user'),
    path('send-email',views.send_email,name='send-email'),
    path('weather',views.weatherview,name='weather'),
    path('weatherinput',views.weatherforecast,name='weatherinput'),
    path('randomotp',views.randomotp,name='randomotp')
]