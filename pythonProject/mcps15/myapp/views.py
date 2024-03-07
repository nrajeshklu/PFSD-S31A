from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Login
from .form import LoginForm, RegistrationForm

def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
        # form.save()
            uid = request.POST['username']  # Fetchinh data from FORM
            upass = request.POST['password']
            flag = Login.objects.filter(username=uid, password=upass).values()
            if flag:
                return  render(request,'home.html')
            else:
                form = LoginForm()
                return render(request, 'login.html', {'form': form})
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def registrationview(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})

def homeview(request):
    return render(request,'home.html')