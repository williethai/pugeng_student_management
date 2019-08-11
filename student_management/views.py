from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from datetime import datetime

import json

from .models import *



class StudentClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Class_Schedule
        fields = '__all__'

@login_required(login_url='/admin/login')
def form_student(request):
    students = StudentFilter(request.GET, queryset=Student.objects.all())
    context = {
        'students': students,
        'gender': Gender.objects.all(),
        'city': City.objects.all(),
        'student_all': Student.objects.all(),
    }
    return render(request, 'form_student.html', context=context)
    
@login_required(login_url='/admin/login')
def add_student(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    try:
        if request.POST.get('gender')!='0':
            gender=Gender.objects.all().get(id=request.POST.get('gender'))
            response['gender'] = gender.__str__()
        else:
            gender=null
            response['gender'] = ""
        if request.POST.get('city')!='0' and request.POST.get('city')!=0 and request.POST.get('city')!='':
            city=City.objects.all().get(id=request.POST.get('city'))
            response['city'] = city.__str__()
        else:
            city=None
            response['city'] = ""
        if request.POST.get('invite_person')!='0' and request.POST.get('invite_person')!=0 and request.POST.get('invite_person')!='':
            invite_person=Student.objects.all().get(id=request.POST.get('invite_person'))
            response['invite_person'] = invite_person.id
            response['invite_person_name'] = invite_person.__str__()
        else:
            invite_person=None
            response['invite_person'] = ""
            response['invite_person_name'] = ""
        if nid == '' or nid == '0' or nid == 0:
            obj = Student.objects.create(
                name=request.POST.get('name'),
                clerical_name=request.POST.get('clerical_name'),
                date_of_birth=request.POST.get('date_of_birth'),
                gender=gender,
                national_id_num=request.POST.get('national_id_num'),
                phone_num=request.POST.get('phone_num'),
                city=city,
                address=request.POST.get('address'),
                invite_person=invite_person,
                emergency_contact_person=request.POST.get('emergency_contact_person'),
                emergency_contact_phone=request.POST.get('emergency_contact_phone'),
                )
        else: #Update new student
            obj = Student.objects.filter(id=str(nid)).update(
                name=request.POST.get('name'),
                clerical_name=request.POST.get('clerical_name'),
                date_of_birth=request.POST.get('date_of_birth'),
                gender=gender,
                national_id_num=request.POST.get('national_id_num'),
                phone_num=request.POST.get('phone_num'),
                city=city,
                address=request.POST.get('address'),
                invite_person=invite_person,
                emergency_contact_person=request.POST.get('emergency_contact_person'),
                emergency_contact_phone=request.POST.get('emergency_contact_phone'),
                )
        response['nid'] = nid

    except Exception as e:
        print(e)
        response['status'] = False
        response['message'] = '用戶輸入錯誤'

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

@login_required(login_url='/admin/login')
def del_student(request):
    ret = {'status': True}
    try:
        nid = request.GET.get('nid')
        Student.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))
@login_required(login_url='/admin/login')
def form_class(request):
    classes = ClassFilter(request.GET, queryset=Class.objects.all())
    #year = 
    context = {
        'classes': classes,
        'student_all': Student.objects.all(),
        'class_status': ['招生中','上課中', '取消', '結束'],
        'year': datetime.today().strftime("%Y"),
        'semester': ['第一期','第二期'],
        'study_time': ['日','夜'],
        'study_status': ['上課中', '取消', '結業'],
    }
    return render(request, 'form_class.html', context=context)

@login_required(login_url='/admin/login')
def add_class(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    try:
        if request.POST.get('supervisor')!=None and request.POST.get('supervisor')!='0' and request.POST.get('supervisor')!=0 and request.POST.get('supervisor')!='':
            print('123')
            supervisor=Student.objects.all().get(id=request.POST.get('supervisor'))
            print(supervisor.__str__())
            response['supervisor'] = supervisor.__str__()
        else:
            supervisor=None
            response['supervisor'] = ""
        
        if request.POST.get('monitor')!=None and request.POST.get('monitor')!='0' and request.POST.get('monitor')!=0 and request.POST.get('monitor')!='':
            
            monitor=Student.objects.all().get(id=request.POST.get('monitor'))
            response['monitor'] = monitor.__str__()
        else:
            
            monitor=None
            response['monitor'] = ""
        
        if request.POST.get('assistant_monitor1')!=None and request.POST.get('assistant_monitor1')!='0' and request.POST.get('assistant_monitor1')!=0 and request.POST.get('assistant_monitor1')!='':
            assistant_monitor1=Student.objects.all().get(id=request.POST.get('assistant_monitor1'))
            response['assistant_monitor1'] = assistant_monitor1.__str__()
        else:
            assistant_monitor1=None
            response['assistant_monitor1'] = ""
        
        if request.POST.get('assistant_monitor2')!=None and request.POST.get('assistant_monitor2')!='0' and request.POST.get('assistant_monitor2')!=0 and request.POST.get('assistant_monitor2')!='':
            assistant_monitor2=Student.objects.all().get(id=request.POST.get('assistant_monitor2'))
            response['assistant_monitor2'] = assistant_monitor2.__str__()
        else:
            assistant_monitor2=None
            response['assistant_monitor2'] = ""
            
        if request.POST.get('assistant_monitor3')!=None and request.POST.get('assistant_monitor3')!='0' and request.POST.get('assistant_monitor3')!=0 and request.POST.get('assistant_monitor3')!='':
            assistant_monitor3=Student.objects.all().get(id=request.POST.get('assistant_monitor3'))
            response['assistant_monitor3'] = assistant_monitor3.__str__()
        else:
            assistant_monitor3=None
            response['assistant_monitor3'] = ""
        print('456')    
        if nid == '' or nid == '0' or nid == 0:
            obj = Class.objects.create(
                name=request.POST.get('name'),
                status=request.POST.get('status_input'),
                teacher=request.POST.get('teacher'),
                supervisor=supervisor,
                monitor=monitor,
                assistant_monitor1=assistant_monitor1,
                assistant_monitor2=assistant_monitor2,
                assistant_monitor3=assistant_monitor3,
                number_of_classes=request.POST.get('number_of_classes'),
                number_of_classes_to_graduate=request.POST.get('number_of_classes_to_graduate'),
                number_of_classes_to_makeup=request.POST.get('number_of_classes_to_makeup'),
                year=request.POST.get('year'),
                semester=request.POST.get('semester'),
                start_date=request.POST.get('start_date'),
                end_date=request.POST.get('end_date'),
                graduation_date=request.POST.get('graduation_date'),
                study_time=request.POST.get('study_time'),
                introduction=request.POST.get('introduction'),
                )
        else: #Update new class
            obj = Class.objects.filter(id=str(nid)).update(
                name=request.POST.get('name'),
                status=request.POST.get('status_input'),
                teacher=request.POST.get('teacher'),
                supervisor=supervisor,
                monitor=monitor,
                assistant_monitor1=assistant_monitor1,
                assistant_monitor2=assistant_monitor2,
                assistant_monitor3=assistant_monitor3,
                number_of_classes=request.POST.get('number_of_classes'),
                number_of_classes_to_graduate=request.POST.get('number_of_classes_to_graduate'),
                number_of_classes_to_makeup=request.POST.get('number_of_classes_to_makeup'),
                year=request.POST.get('year'),
                semester=request.POST.get('semester'),
                start_date=request.POST.get('start_date'),
                end_date=request.POST.get('end_date'),
                graduation_date=request.POST.get('graduation_date'),
                study_time=request.POST.get('study_time'),
                introduction=request.POST.get('introduction'),
                )
        response['nid'] = nid

    except Exception as e:
        response['message'] = '用戶輸入錯誤'
        response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

@login_required(login_url='/admin/login')
def del_class(request):
    ret = {'status': True}
    try:
        nid = request.GET.get('nid')
        Class.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))
@login_required(login_url='/admin/login')
def add_student_to_class(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    try:
        if request.POST.get('student')!=None and request.POST.get('student')!='0' and request.POST.get('student')!=0 and request.POST.get('student')!='':
            student=Student.objects.all().get(id=request.POST.get('student'))
            response['student'] = student.__str__()
        else:
            student=None
            response['student'] = ""
            
        if request.POST.get('invite_person')!=None and request.POST.get('invite_person')!='0' and request.POST.get('invite_person')!=0 and request.POST.get('invite_person')!='':
            invite_person=Student.objects.all().get(id=request.POST.get('invite_person'))
            response['invite_person'] = invite_person.__str__()
        else:
            invite_person=None
            response['invite_person'] = ""
            
        if request.POST.get('group_of_student')!=None and request.POST.get('group_of_student')!='0' and request.POST.get('group_of_student')!=0 and request.POST.get('group_of_student')!='':
            group_of_student=Class_Group.objects.all().get(id=request.POST.get('group_of_student'))
            response['group_of_student'] = student.__str__()
        else:
            group_of_student=None
            response['group_of_student'] = ""
        if nid == '' or nid == '0' or nid == 0:
            obj = Student_Class.objects.create(
                student=student,
                class_of_student=Class.objects.all().get(id=request.POST.get('class_of_student')),
                status=request.POST.get('study_status_input'),
                invite_person=invite_person,
                group_of_student=group_of_student,
                present_check=0,
                date_joined=request.POST.get('date_joined'),
                )
        else:
            obj = Student_Class.objects.filter(id=str(nid)).update(
                student=student,
                class_of_student=Class.objects.all().get(id=request.POST.get('class_of_student')),
                status=request.POST.get('study_status_input'),
                invite_person=invite_person,
                group_of_student=group_of_student,
                present_check=0,
                date_joined=request.POST.get('date_joined'),
                )
        response['nid'] = nid

    except Exception as e:
        print(e)
        response['message'] = '用戶輸入錯誤'
        if 'UNIQUE constraint' in str(e):
            response['message'] = '此學員已加入'
        response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)
@login_required(login_url='/admin/login')
def form_present_check(request):
    classes = ClassStudentPresentFilter(request.GET, queryset=Class.objects.all())
    
    if request.method == 'POST':
        print('form_present_check')
        
    context = {
        'classes': classes,
    }
    return render(request, 'form_present_check.html', context=context)

@login_required(login_url='/admin/login')
def check_in_qrcode(request):
    return render(request, 'check_in_qrcode.html')

@login_required(login_url='/admin/login')
def name_card_pdf(request, id):
    
    student_class = Student_Class.objects.all().filter(class_of_student=id)
    context = {
        'student_class': student_class,
    }
    return render(request, 'name_card.html', context=context)

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
