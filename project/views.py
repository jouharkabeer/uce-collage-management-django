from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages, auth



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('/admin_login')
    return render(request, "admin_home.html")


# Create your views here.

def index(request):
    return render(request, "index.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/admin_home')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/admin_login')
    return render(request, "admin_login.html")

def student_login(request):
    return render(request, "student_login.html")

def faculty_login(request):
    return render(request, "faculty_login.html")

def alumni_login(request):
    return render(request, "alumni_login.html")

def Logout(request):
    logout(request)
    return redirect('/')