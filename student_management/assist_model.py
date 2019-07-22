from django.db import models
from django.contrib import admin

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=5, default='')
    def __str__(self):
        return self.gender
        
class Class_Status(models.Model):
    status = models.CharField(max_length=60)
    create_at = models.DateTimeField()
    def __str__(self):
        return self.status
        
class Student_Class_Status(models.Model):
    status = models.CharField(max_length=10, default='')
    def __str__(self):
        return self.status
    
class Volunteer_Status(models.Model):
    status = models.CharField(max_length=60)
    create_at = models.DateTimeField()
    def __str__(self):
        return self.status
        
        
        
##############Model Admin
class Gender_Admin(admin.ModelAdmin):
    list_display = (['gender'])
    
class Class_Status_Admin(admin.ModelAdmin):
    list_display = (['status'])
    
class Student_Class_Status_Admin(admin.ModelAdmin):
    list_display = (['status'])
    
class Volunteer_Status_Admin(admin.ModelAdmin):
    list_display = (['status'])