from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("logout", views.Logout, name="logout"),

    
    #Admin Urls
    path('admin_login', views.admin_login, name='admin login' ),
    path('admin_home', views.admin_home, name='admin login' ),

    #Student Urls
    path('student_login/', views.student_login, name='student login' ),

    #Faculty Urls
    path('faculty_login/', views.faculty_login, name='faculty login' ),

    #Alumni Urls
    path('alumni_login/', views.alumni_login, name='alumni login' ),
]