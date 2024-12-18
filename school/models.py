from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.password} -{self.email}"
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.password} -{self.subject}"
    
    
class Grades(models.Model):
    student = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    partial1 = models.CharField(max_length=10)
    partial2 = models.CharField(max_length=10)
    partial3 = models.CharField(max_length=10)
    ordinary = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student.email} - {self.subject}: {self.partial1}, {self.partial2}, {self.partial3}, {self.ordinary}"
