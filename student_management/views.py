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
        if request.POST.get('city')!='0' and request.POST.get('city')!=0:
            city=City.objects.all().get(id=request.POST.get('city'))
            response['city'] = city.__str__()
        else:
            city=None
            response['city'] = ""
        if request.POST.get('invite_person')!='0' and request.POST.get('invite_person')!=0:
            invite_person=Student.objects.all().get(id=request.POST.get('invite_person'))
            response['invite_person'] = invite_person.__str__()
        else:
            invite_person=None
            response['invite_person'] = ""
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
        else:
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
        response['status'] = False
        response['message'] = '用户输入错误'

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
    context = {
        'classes': classes,
    }
    return render(request, 'form_class.html', context=context)

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
