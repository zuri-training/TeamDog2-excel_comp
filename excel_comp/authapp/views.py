from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, logout

# Create your views here.
def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password_confirm']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=email, password=password,email=email,first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "User created successfully")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
    else:   
        return render(request, 'signUp.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login successful")
            #return redirect("nextpage")
            return redirect("login")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, 'logIn.html')


def logoutUser(request):
    logout(request)
    return redirect('login')