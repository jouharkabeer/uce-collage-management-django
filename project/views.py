from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages, auth
import re





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
            messages.info(request, "!!!Invalid credentials")
            return redirect('/admin_login')
    return render(request, "admin_login.html")



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('/admin_login')
    return render(request, "admin_home.html")

def all_students(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    students = Student.objects.all()
    return render(request, "all_students.html", {'students':students})


def student_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                user1 = Student.objects.get(user=user)
                if user1.type == "student":
                    if user1.status == "pending":
                        return render(request,"user_login.html",{"msg":"You need to be wait undil admin approval"})
                    elif user1.status=='Rejected':
                        return render(request,"user_login.html",{"msg":"You account is blocked by admin"})
                    else:
                        login(request, user)
                        return redirect("/student_home")
            else:
                thank = True
                return render(request, "student_login.html", {"thank":thank})
    return render(request, "student_login.html")

def student_signup(request):
    if request.method == "POST":
        username = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        aadhar_number = request.POST.get('aadhar_id')

        if username and first_name and last_name and password1 and password2 and phone and gender and image:
            # Validate phone number
            pattern = re.compile("(0|91)?[7-9][0-9]{9}")
            if not pattern.match(phone):
                return render(request, "student_signup.html", {"msg": "Invalid mobile number"})

            # Validate Aadhar number
            if not len(aadhar_number) == 12:
                return render(request, "student_signup.html", {"msg": "Invalid Aadhar number"})

            # Check if passwords match
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('/student_signup')

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return render(request, "student_signup.html", {"msg": "Username already exists"})

            # Create user
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=username, password=password1)

            # Create student
            student = Student.objects.create(name=user, phone=phone, gender=gender, image=image, type="student", aadhaar_number=aadhar_number, status="pending")
            
            user.save()
            student.save()
            # Redirect to login page
            return redirect("/student_login")
        else:
            return render(request, "student_signup.html", {"msg": "Please fill all fields"})

    return render(request, "student_signup.html")


def student_home(request):
    if not request.user.is_authenticated:
        return redirect('/student_login')
    return render(request, "student_home.html")

def faculty_login(request):
    return render(request, "faculty_login.html")

def alumni_login(request):
    return render(request, "alumni_login.html")

def Logout(request):
    logout(request)
    return redirect('/')