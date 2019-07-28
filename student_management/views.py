from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *

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
    
    context = {
        'classes': classes,
    }
    return render(request, 'form_present_check.html', context=context)
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