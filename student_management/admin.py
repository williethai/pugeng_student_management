from django.contrib import admin
from .models import *
#from .forms import ItemForm, StudentForm
# Register your models here.

class Student_Class_Inline(admin.TabularInline):
    model  = Student_Class
    extra  = 0
    readonly_fields = ["student_qr_code"]
    
class Class_Group_Inline(admin.TabularInline):
    model  = Class_Group
    extra  = 0

class Class_Schedule_Inline(admin.TabularInline):
    model  = Class_Schedule
    extra  = 0
    
class StudentAdmin(admin.ModelAdmin):
    list_display = (['name', 'clerical_name', 'date_of_birth', 'gender', 'national_id_num', 'phone_num', 'city', 'address', 'invite_person', 'emergency_contact_person', 'emergency_contact_phone', 'list_classes'])
    inlines = (Student_Class_Inline,)
    fields = (
        ('name', 'clerical_name'),
        ('date_of_birth', 'gender'),
        ('national_id_num', 'phone_num'),
        ('city', 'address'), 
        ('invite_person'),
        ('emergency_contact_person', 'emergency_contact_phone'),
        ('date_joined'),
    )
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        return super(StudentAdmin, self).changeform_view(request, object_id, extra_context=extra_context)
    #form = StudentForm
class ClassAdmin(admin.ModelAdmin):
    #list_display = (['name', 'list_students'])
    inlines = (Class_Group_Inline, Class_Schedule_Inline, Student_Class_Inline, )
    fields = (
        ('name', 'status'),
        ('monitor', 'number_of_classes'),
        ('year', 'semester'),
        ('start_date', 'end_date', 'study_time'),
        ('introduction'),
    )
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        return super(ClassAdmin, self).changeform_view(request, object_id, extra_context=extra_context)
class ClassGroupAdmin(admin.ModelAdmin):
    list_display = (['class_of_group', 'name', 'leader', 'assistant_leader1'])

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = (['id', '__str__'])

class StudentClassScheduleAdmin(admin.ModelAdmin):
    list_display = (['class_of_student', 'student', 'present_check'])

    
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Class_Group, ClassGroupAdmin)
admin.site.register(Student_Class_Schedule)
admin.site.register(Class_Schedule, ClassScheduleAdmin)

admin.site.register(Gender, Gender_Admin)
admin.site.register(Class_Status, Class_Status_Admin)
admin.site.register(Student_Class_Status, Student_Class_Status_Admin)
admin.site.register(Volunteer_Status, Volunteer_Status_Admin)
admin.site.register(City, City_Admin)
admin.site.register(StudyTime, StudyTime_Admin)
admin.site.register(StudyYear, StudyYear_Admin)
admin.site.register(StudySemester, StudySemester_Admin)

admin.site.register(Student_Class)

admin.site.site_header = "學員管理幫手";
admin.site.site_title = "學員管理幫手";
admin.site.index_title = "學員資訊"
admin.site.site_url = None