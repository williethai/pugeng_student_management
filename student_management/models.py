from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import django_filters
from .assist_model import *

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True, verbose_name='學員編號')
    name = models.CharField(max_length=60, default='', verbose_name='姓名')
    clerical_name = models.CharField(max_length=60, default='', blank=True, verbose_name='法名')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default='', related_name='gender_set', verbose_name='性別')
    national_id_num = models.CharField(max_length=20, default='', blank=True, verbose_name='統一編號')
    phone_num = models.CharField(max_length=20, default='', verbose_name='電話')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name='city_set', verbose_name='市')
    #area = models.CharField(max_length=100, default='', blank=True, verbose_name='區')
    address = models.CharField(max_length=100, default='', blank=True, verbose_name='地址')
    invite_person = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='invite_person_set', blank=True, verbose_name='介紹人')
    emergency_contact_person = models.CharField(max_length=60, default='', blank=True, verbose_name='緊急聯絡人')
    emergency_contact_phone = models.CharField(max_length=20, default='', blank=True, verbose_name='緊急聯絡電話')
    #create_at = models.DateTimeField()
    def list_classes(self):
        return "\n".join(str(c.name + ':' + c.status.status) for c in self.class_of_student.all())
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "學員"

class StudentFilter(django_filters.FilterSet):
    #gender = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Student
        fields = ['gender', 'city']
        
class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='', verbose_name='名稱')
    status = models.ForeignKey(Class_Status, on_delete=models.CASCADE, default='', related_name='class_status_set', verbose_name='狀態')
    monitor = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='class_monitor_set', verbose_name='總學員長', null=True, blank=True)
    students = models.ManyToManyField(Student, through='Student_Class', blank=True, related_name='class_of_student', verbose_name='班中學員')
    number_of_classes = models.IntegerField(default=0, verbose_name='班總數', null=True, blank=True)
    year = models.ForeignKey(StudyYear, on_delete=models.CASCADE, null=True, blank=True, related_name='study_year_set', verbose_name='年')
    semester = models.ForeignKey(StudySemester, on_delete=models.CASCADE, null=True, blank=True, related_name='study_semester_set', verbose_name='期')
    start_date = models.DateField(null=True, blank=True, verbose_name='開始日期')
    end_date = models.DateField(null=True, blank=True, verbose_name='結束日期')
    study_time = models.ForeignKey(StudyTime, on_delete=models.CASCADE, null=True, blank=True, related_name='study_time_set', verbose_name='上課時間')
    #create_at = models.DateTimeField()
    introduction = models.CharField(max_length=2000, default='', blank=True, null=True)
    def list_students(self):
        return "\n".join(str(c for c in self.students.all()) )
    @property
    def to_str(self):
        return str(str(self.year) + " - " +str(self.semester) + ' - ' + self.name)
    
    def __str__(self):
        return str(str(self.year) + " - " +str(self.semester) + ' - ' + self.name)
        #return self.name
    class Meta:
        verbose_name_plural = "班別"
        
class ClassFilter(django_filters.FilterSet):
    #gender = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Class
        fields = ['status', 'monitor', 'year', 'semester', 'study_time']
class ClassStudentPresentFilter(django_filters.FilterSet):
    #gender = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Class
        fields = ['name', 'year', 'semester', 'study_time']
class Class_Schedule(models.Model):
    class_to_schedule = models.ForeignKey(Class, on_delete=models.CASCADE, default='', related_name='scheduled_class_set', verbose_name='班別')
    study_time = models.DateField(null=True, blank=True, default='', verbose_name='上課時間')
    study_location = models.CharField(max_length=100, default='精舍', null=True, blank=True, verbose_name='上課地點')
    content  = models.CharField(max_length=2000, default='', null=True, blank=True, verbose_name='上課內容')
    @property
    def get_date(self):
        return str(self.study_time.strftime('%m/%d'))

    def __str__(self):
        return str(self.class_to_schedule.__str__() + '-' + str(self.study_time))

        
class Class_Group(models.Model):
    name = models.CharField(max_length=60, default='', verbose_name='組別')
    class_of_group = models.ForeignKey(Class, on_delete=models.CASCADE, default='', related_name='class_group_set', verbose_name='班別')
    leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='group_leader_set', verbose_name='學員長')
    assistant_leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='assist_group_leader_set', verbose_name='副學員長')
    class Meta:
        verbose_name_plural = "班中組別"
    def __str__(self):
        return str(self.class_of_group.__str__() + ' 組: ' + self.name)


#Many-to-Many stduent & class group relationship
class Student_Class(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='in_class_student_set', verbose_name='學員名稱')
    class_of_student = models.ForeignKey(Class, on_delete=models.CASCADE, default='', related_name='student_with_class_set', blank=True)
    date_joined = models.DateField(null=True, blank=True, verbose_name='參加日期')
    group_of_student = models.ForeignKey(Class_Group, on_delete=models.CASCADE, default='', related_name='group_of_student_in_class', blank=True, null=True, verbose_name='組別')
    status = models.ForeignKey(Student_Class_Status, on_delete=models.CASCADE, default='', related_name='student_class_status_set', verbose_name='上課狀態')
    present_check = models.IntegerField(default=0, blank=True, verbose_name='出席')
    #create_at = models.DateTimeField(blank=True)
    class Meta:
        verbose_name_plural = "班中學員"
        
#Many-to-Many stduent & class & class schedule session group relationship
class Student_Class_Schedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='in_student_class_schedule_set', verbose_name='學員名稱')
    class_of_student = models.ForeignKey(Class, on_delete=models.CASCADE, default='', related_name='student_of_scheduled_class')
    scheduled_class = models.ForeignKey(Class_Schedule, on_delete=models.CASCADE, default='', related_name='scheduled_class', blank=True, null=True, verbose_name='班')
    present_check = models.BooleanField(default=False, verbose_name='出席')
    #create_at = models.DateTimeField(blank=True)
    class Meta:
        verbose_name_plural = "班中學員出席"

class Volunteer_Group(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='', verbose_name='名稱')
    leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='volunteer_group_leader_set', verbose_name='組長')
    assist_leader = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='volunteer_group_assist_leader_set', verbose_name='副組長')
    volunteer_students = models.ManyToManyField(Student, through='Student_Volunteer_Group', verbose_name='志工學員')
    #create_at = models.DateTimeField()
    #def list_students(self):
    #    return "\n".join(str(c for c in self.students.all()) )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "志工組"

#Many-to-Many stduent & volunteer group relationship
class Student_Volunteer_Group(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='in_student_volunteer_group_student_set', verbose_name='志工學員')
    volunteer_group = models.ForeignKey(Volunteer_Group, on_delete=models.CASCADE, default='', related_name='volunteer_group_set', verbose_name='志工組')
    status = models.ForeignKey(Volunteer_Status, on_delete=models.CASCADE, default='', related_name='volunteer_status_set', verbose_name='活動狀態')
    date_joined = models.DateField(default='0000-00-00', verbose_name='參加日期')
    #create_at = models.DateTimeField()
    class Meta:
        verbose_name_plural = "志工組中學員"