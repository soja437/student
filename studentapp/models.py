from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    student_name=models.CharField(max_length=255)
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField()
    student_email=models.EmailField()
    joining_date=models.DateField()
    qualification=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    mobileno=models.CharField(max_length=255)