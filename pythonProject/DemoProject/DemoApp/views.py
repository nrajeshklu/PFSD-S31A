import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import RegistrationForm, LoginForm, AdminForm
from .models import User,Login
from django.core.mail import send_mail, EmailMessage
import random
import string


# Create your views here.
def demoFunction(request):
    return HttpResponse('This is DemoApp1')
def homefun(request):
    return render(request,'home.html')
def loginfun(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uid = request.POST['username']
            upass=request.POST['password']
            flag=Login.objects.filter(username=uid,password=upass).values()
            if flag:
                return redirect('home')
            else:
                form = LoginForm()
                return render(request, 'login.html', {'form': form})
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html',{'form':form})
def regfun(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})
def adminfun(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['auser'] == 'admin':
                if form.cleaned_data['apassword'] == 'admin':
                    return render(request,'show.html',{'users':users})

        else:
            form = AdminForm()
            return render(request, 'adminreg.html', {'form': form})
    else:
        form = AdminForm()
    return render(request, 'adminreg.html',{'form':form})

def aboutusfun(request):
    return render(request,'aboutus.html')

def show_users(request):
    users = User.objects.all()
    return render(request, 'show.html', {'users':users})

def edit_user(request,pk):
    users = User.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            users.fullname = request.POST['fname']
            users.email = request.POST['email']
            users.username = request.POST['uname']
            users.password = request.POST['upass']
            users.mobileno = request.POST['mno']
            users.location = request.POST['loc']
            users.save()
            print("Updation success")
            users = User.objects.all()
            #return redirect("show-users")
            return render(request, 'show.html', {'users': users})
    return render(request, 'edit.html', {'users':users})

def delete_user(request, pk):
    users = User.objects.get(id=pk)
    if request.method == 'POST':
        users.delete()
        print("Deletion succcess")
        users = User.objects.all()
        return render(request, 'show.html', {'users': users})
    return render(request, 'delete.html', {'users':users})

def send_email(request):
    subject = 'SampleMailFromDjangoApp'
    message = 'Hi! Welcome to Email Services provide by Django!!'
    from_email = 'nrajeshmtech@gmail.com'
    recipient_list = ['rajeshnbtech@gmail.com', 'nrajeshbtech@gmail.com']
    #send_mail(subject, message, from_email, recipient_list)

    html_content = '<h1>This is HTML content Generated from Django Mail services </h1>'
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.content_subtype = 'html'
    email.attach(html_content, "text/html")
    email.send()
    return render(request,'mailsent.html')

def weatherview(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '98c9fe0696484df631f05ef073b66aa4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html',
                      {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})
    # else:
    #     return render(request, 'weatherappinput.html')

def weatherforecast(request):
       return render(request, 'weatherappinput.html')

def randomotp(request):
    if request.method=="POST":
        number1=request.POST['rnum']
        number2=int(number1)
        results = ''.join(random.sample(string.digits,number2))
        print(results)
        return render(request,'randomotp.html',{'results':results})
    else:
        return render(request, 'randomotp.html',)
