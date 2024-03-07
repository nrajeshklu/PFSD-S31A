from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def register_user(request):
    # users = User()
    if request.method == 'POST':
            print(request.POST)
            fullname = request.POST['fname']
            email = request.POST['umail']
            username = request.POST['uname']
            password = request.POST['upass']
            mobileno = request.POST['mnum']
            address = request.POST['address']
            users = User(id,fullname,email,username,password,mobileno,address)
            users.save()
            print("Inserted successfully")
            users = User.objects.all()
            return render(request,'UserRegistration.html',{'users':users})
    else:
        return render(request,'UserRegistration.html')

def homepage(request):
    return render(request,'home.html')