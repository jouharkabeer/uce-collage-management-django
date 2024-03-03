from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
# Create your views here.

def index(request):
    return render(request, "index.html")

def admin_login(request):
    return render(request, "admin_login.html")

def student_login(request):
    return render(request, "student_login.html")

def faculty_login(request):
    return render(request, "faculty_login.html")

def alumni_login(request):
    return render(request, "alumni_login.html")