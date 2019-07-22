from django.contrib import admin
from .models import *
#from .forms import ItemForm, StudentForm
# Register your models here.

class Student_Class_Inline(admin.TabularInline):
    model  = Student_Class
    extra  = 1
    
class StudentAdmin(admin.ModelAdmin):
    #list_display = (['name'])
    inlines = (Student_Class_Inline,)
    #form = StudentForm
class ClassAdmin(admin.ModelAdmin):
    #list_display = (['name', 'list_students'])
    inlines = (Student_Class_Inline,)

admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Gender, Gender_Admin)
admin.site.register(Class_Status, Class_Status_Admin)
admin.site.register(Student_Class_Status, Student_Class_Status_Admin)
admin.site.register(Volunteer_Status, Volunteer_Status_Admin)

admin.site.site_header = "學員管理幫手";
admin.site.site_title = "學員管理幫手";
admin.site.index_title = "學員資訊"
admin.site.site_url = None