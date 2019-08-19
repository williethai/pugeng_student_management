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
class MakeUpClassBookingRecord(models.Model):
    make_up_date = models.DateField(null=True, blank=True)
    make_up_time = models.CharField(max_length=10, default='', blank=True, null=True)
    booking_record = models.IntegerField(default=0, blank=True)
    class Meta:
        unique_together = ('make_up_date', 'make_up_time')

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

class MakeUpClassBookingRecord_Admin(admin.ModelAdmin):
    list_display = (['make_up_date', 'make_up_time', 'booking_record'])