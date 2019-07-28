from django.urls import path

from .views import *

urlpatterns = [
    path('form_student', form_student, name='form_student'),
    path('form_class', form_class, name='form_class'),
    path('form_present_check', form_present_check, name='form_present_check'),
    path('', HomePageView.as_view(), name='home'),
    path('new', StudentCreate.as_view(), name='student_new'),
    path('view/<int:pk>', StudentDetail.as_view(), name='student_detail'),
]