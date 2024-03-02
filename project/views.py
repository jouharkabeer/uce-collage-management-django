from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
# Create your views here.

def index(request):
    return render(request, "index.html")