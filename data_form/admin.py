from django.contrib import admin
from student_management.models import *

class ClassAdmin():
    exclude = ('name',)
    
#admin.site.register(Class, ClassAdmin)

admin.site.site_header = "學員管理幫手";
admin.site.site_title = "學員管理幫手";
admin.site.index_title = "學員資訊"
admin.site.site_url = None