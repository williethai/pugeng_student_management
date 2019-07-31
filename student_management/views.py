from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


from .models import *

class StudentClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Class_Schedule
        fields = '__all__'

def form_student(request):
    #students = Student.objects.all()
    students = StudentFilter(request.GET, queryset=Student.objects.all())
    context = {
        'students': students,
    }
    return render(request, 'form_student.html', context=context)
    
def form_class(request):
    classes = ClassFilter(request.GET, queryset=Class.objects.all())
    context = {
        'classes': classes,
    }
    return render(request, 'form_class.html', context=context)

def form_present_check(request):
    classes = ClassStudentPresentFilter(request.GET, queryset=Class.objects.all())
    
    if request.method == 'POST':
        print('form_present_check')
        
    context = {
        'classes': classes,
    }
    return render(request, 'form_present_check.html', context=context)

def check_in_qrcode(request):
    return render(request, 'check_in_qrcode.html')

class StudentClassSchedulePartialUpdateView(GenericAPIView, UpdateModelMixin):

    queryset = Student_Class_Schedule.objects.all()
    serializer_class = StudentClassScheduleSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
        
    
    #def perform_update(self, serializer):
    #    instance = serializer.save()
    #    self.post_save(instance)
        
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'clerical_name', 'date_of_birth', 'gender', 'national_id_num', 'phone_num', 'address', 'invite_person', 'emergency_contact_person', 'emergency_contact_phone']
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'clerical_name', 'date_of_birth', 'gender', 'national_id_num', 'phone_num', 'address', 'invite_person', 'emergency_contact_person', 'emergency_contact_phone']
    success_url = reverse_lazy('student_list')