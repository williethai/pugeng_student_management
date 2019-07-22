from django.db import models
from .assist_model import *

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    clerical_name = models.CharField(max_length=60, default='')
    date_of_birth = models.DateTimeField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default='', related_name='gender_set')
    national_id_num = models.CharField(max_length=20, default='')
    phone_num = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    invite_person = models.ForeignKey('self', on_delete=models.CASCADE, default='', related_name='invite_person_set')
    emergency_contact_person = models.CharField(max_length=60, default='')
    emergency_contact_phone = models.CharField(max_length=20, default='')
    create_at = models.DateTimeField()
    def list_classes(self):
        return "\n".join(str(c for c in self.publications.all()))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "學員"
        
class Class(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    status = models.ForeignKey(Class_Status, on_delete=models.CASCADE, default='', related_name='class_status_set')
    monitor = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='class_monitor_set')
    students = models.ManyToManyField(Student, through='Student_Class')
    number_of_classes = models.IntegerField(default=0)
    year = models.CharField(max_length=5, default='')
    semester = models.CharField(max_length=5, default='')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    create_at = models.DateTimeField()
    introduction = models.CharField(max_length=2000, default='')
    def list_students(self):
        return "\n".join(str(c for c in self.students.all()) )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "班別"
        
class Class_Schedule(models.Model):
    class_to_schedule = models.ForeignKey(Class, on_delete=models.CASCADE, default='', related_name='scheduled_class_set')
    content  = models.CharField(max_length=2000, default='')

#Many-to-Many stduent & class group relationship
class Student_Class(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='in_class_student_set')
    class_of_student = models.ForeignKey(Class, on_delete=models.CASCADE, default='', related_name='student_with_class_set')
    date_joined = models.DateField(default='0000-00-00')
    class_group = models.CharField(max_length=5, default='')
    status = models.ForeignKey(Student_Class_Status, on_delete=models.CASCADE, default='', related_name='student_class_status_set')
    present_check = models.IntegerField(default=0)
    create_at = models.DateTimeField()
    class Meta:
        verbose_name_plural = "學員-班別新增"
        
class Class_Group(models.Model):
    name = models.CharField(max_length=60, default='')
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, default='', related_name='class_group_set')
    leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='group_leader_set')
    assistant_leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='assist_group_leader_set')
    
class Volunteer_Group(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='volunteer_group_leader_set')
    assist_leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='volunteer_group_assist_leader_set')
    volunteer_students = models.ManyToManyField(Student, through='Student_Volunteer_Group')
    create_at = models.DateTimeField()
    #def list_students(self):
    #    return "\n".join(str(c for c in self.students.all()) )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "功德組"

#Many-to-Many stduent & volunteer group relationship
class Student_Volunteer_Group(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='in_student_volunteer_group_student_set')
    volunteer_group = models.ForeignKey(Volunteer_Group, on_delete=models.CASCADE, default='', related_name='volunteer_group_set')
    status = models.ForeignKey(Volunteer_Status, on_delete=models.CASCADE, default='', related_name='volunteer_status_set')
    date_joined = models.DateField(default='0000-00-00')
    create_at = models.DateTimeField()
    class Meta:
        verbose_name_plural = "學員-班別新增"