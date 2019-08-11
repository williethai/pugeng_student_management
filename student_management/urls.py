from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    path('form_student', form_student, name='form_student'),
    path('add_student', add_student, name='add_student'),
    path('del_student', del_student, name='del_student'),
    path('form_class', form_class, name='form_class'),
    path('add_class', add_class, name='add_class'),
    path('del_class', del_class, name='del_class'),
    path('add_student_to_class', add_student_to_class, name='add_student_to_class'),
    path('form_present_check', form_present_check, name='form_present_check'),
    path('check_in_qrcode', check_in_qrcode, name='check_in_qrcode'),
    path('name_card_pdf/<int:id>', name_card_pdf, name='name_card_pdf'),
    url(r'^api/student_class_schedule/update_student_attendance/(?P<pk>\d+)/$', StudentClassSchedulePartialUpdateView.as_view(), name='student_class_schedule_partial_update'),
    url(r'^bucketlists/$', StudentClassSchedulePartialUpdateView.as_view(), name="create"),
    path('', HomePageView.as_view(), name='home'),
]