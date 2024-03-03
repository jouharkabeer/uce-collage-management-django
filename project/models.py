from operator import mod
from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=10)
    semester = models.CharField(max_length=15)
    aadhaar_number = models.CharField(max_length=16,blank=True,null=True)
    status = models.CharField(max_length=20,null=True,blank=True)
    

    def __str__(self):
        return self.user.first_name
    
class Alumni(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    year_of_passout = models.IntegerField(null=True)
    image = models.ImageField(upload_to="")
    
    

class Faculty(models.Model):
    name = models.CharField(max_length=15)
    Department = models.CharField(max_length=15)
    image = models.ImageField(upload_to="")


class Mark(models.Model):
    sid = models.ForeignKey(Student, to_field='sid', on_delete=models.CASCADE)
    sub1 = models.IntegerField(null=True)
    sub2 = models.IntegerField(null=True)
    sub3 = models.IntegerField(null=True)
    sub4 = models.IntegerField(null=True)
    sub5 = models.IntegerField(null=True)
    attendence = models.FloatField

class Alumnipost(models.Model):
    aid = models.ForeignKey(Alumni, to_field='aid', on_delete=models.CASCADE)
    link = models.URLField(null=True)
