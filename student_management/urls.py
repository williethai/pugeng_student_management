from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    path('form_student', form_student, name='form_student'),
    path('form_class', form_class, name='form_class'),
    path('form_present_check', form_present_check, name='form_present_check'),
    path('check_in_qrcode', check_in_qrcode, name='check_in_qrcode'),
    url(r'^api/student_class_schedule/update_student_attendance/(?P<pk>\d+)/$', StudentClassSchedulePartialUpdateView.as_view(), name='student_class_schedule_partial_update'),
    url(r'^bucketlists/$', StudentClassSchedulePartialUpdateView.as_view(), name="create"),
    path('', HomePageView.as_view(), name='home'),
    path('new', StudentCreate.as_view(), name='student_new'),
    path('view/<int:pk>', StudentDetail.as_view(), name='student_detail'),
]