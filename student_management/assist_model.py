from django.db import models
from django.contrib import admin

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=5, default='')
    def __str__(self):
        return self.gender
        
class Class_Status(models.Model):
    status = models.CharField(max_length=60)
    #create_at = models.DateTimeField()
    def __str__(self):
        return self.status
        
class Student_Class_Status(models.Model):
    status = models.CharField(max_length=10, default='')
    def __str__(self):
        return str(self.status)
    
class Volunteer_Status(models.Model):
    status = models.CharField(max_length=60)
    #create_at = models.DateTimeField()
    def __str__(self):
        return self.status
        
class City(models.Model):
    name = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.name
        
class StudyTime(models.Model):
    time = models.CharField(max_length=10, default='')
    def __str__(self):
        return self.time
        
class StudyYear(models.Model):
    year = models.PositiveIntegerField(default=2019)
    def __str__(self):
        return str(self.year)
        
class StudySemester(models.Model):
    semester = models.CharField(max_length=10, default='')
    def __str__(self):
        return self.semester
##############Model Admin
class Gender_Admin(admin.ModelAdmin):
    list_display = (['gender'])
    
class Class_Status_Admin(admin.ModelAdmin):
    list_display = (['status'])
    
class Student_Class_Status_Admin(admin.ModelAdmin):
    list_display = (['status'])
    
class Volunteer_Status_Admin(admin.ModelAdmin):
    list_display = (['status'])
    
class City_Admin(admin.ModelAdmin):
    list_display = (['name'])
    
class StudyTime_Admin(admin.ModelAdmin):
    list_display = (['time'])

class StudyYear_Admin(admin.ModelAdmin):
    list_display = (['year'])
    
class StudySemester_Admin(admin.ModelAdmin):
    list_display = (['semester'])