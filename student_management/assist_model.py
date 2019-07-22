from django.db import models

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=5, default='')
        
class Class_Status(models.Model):
    status = models.CharField(max_length=60)
    create_at = models.DateTimeField()
    def __str__(self):
        return self.name
        
class Student_Class_Status(models.Model):
    status = models.CharField(max_length=10, default='')
    
class Volunteer_Status(models.Model):
    status = models.CharField(max_length=60)
    create_at = models.DateTimeField()
    def __str__(self):
        return self.name