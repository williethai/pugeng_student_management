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

from datetime import datetime, date, timedelta
from dateutil.relativedelta import *

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
def form_class_detail(request, id):
    #classes = ClassFilter(request.GET, queryset=Class.objects.all())
    class_i = Class.objects.all().get(id=id)
    context = {
        'class_i': class_i,
        'student_all': Student.objects.all(),
        'class_status': ['招生中','上課中', '取消', '結束'],
        'year': datetime.today().strftime("%Y"),
        'semester': ['第一期','第二期'],
        'study_time': ['日','夜'],
        'study_status': ['上課中', '取消', '結業'],
    }
    return render(request, 'form_class_detail.html', context=context)

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
            response['nid'] = obj.id
            response['start_date'] = obj.start_date
            response['graduation_date'] = obj.graduation_date
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
            response['start_date'] = request.POST.get('start_date')
            response['graduation_date'] = request.POST.get('graduation_date')
            response['nid'] = nid

    except Exception as e:
        print(e)
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
def add_class_schedule(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    class_to_schedule_id = request.POST.get('class_to_schedule')
    study_time = request.POST.get('study_time')
    print(class_to_schedule_id)
    print(study_time)
    try:
        
        if class_to_schedule_id != None and class_to_schedule_id!='0' and class_to_schedule_id!=0 and class_to_schedule_id!='':
            class_to_schedule=Class.objects.all().get(id=class_to_schedule_id)
        else:
            response['message'] = '用戶輸入錯誤'
        if study_time == None and study_time=='0' and study_time==0 and study_time=='':
            response['message'] = '用戶輸入錯誤'
            
        if nid == '' or nid == '0' or nid == 0 or nid == None:
            obj = Class_Schedule.objects.create(
                class_to_schedule=class_to_schedule,
                study_time=study_time,
                )
            response['nid'] = obj.id
        else:
            pass
        

    except Exception as e:
        print(e)
        response['message'] = '用戶輸入錯誤'
        if 'UNIQUE constraint' in str(e):
            response['message'] = '重複堂'
        response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)
@login_required(login_url='/admin/login')
def del_scheduled_class(request):
    ret = {'status': True}
    try:
        nid = request.POST.get('nid')
        Class_Schedule.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))
    
@login_required(login_url='/admin/login')
def add_group_to_class(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    class_of_group = request.POST.get('class_of_group')
    leader = request.POST.get('leader')
    assistant_leader1 = request.POST.get('assistant_leader1')
    assistant_leader2 = request.POST.get('assistant_leader2')
    assistant_leader3 = request.POST.get('assistant_leader3')

    try:
        if class_of_group!=None and class_of_group!='0' and class_of_group!=0 and class_of_group!='':
            class_of_group=Class.objects.all().get(id=class_of_group)
        else:
            class_of_group=None
            
        if leader!=None and leader!='0' and leader!=0 and leader!='':
            leader=Student.objects.all().get(id=leader)
        else:
            leader=None
        
        if assistant_leader1!=None and assistant_leader1!='0' and assistant_leader1!=0 and assistant_leader1!='':
            assistant_leader1=Student.objects.all().get(id=assistant_leader1)
        else:
            assistant_leader1=None
        
        if assistant_leader2!=None and assistant_leader2!='0' and assistant_leader2!=0 and assistant_leader2!='':
            assistant_leader2=Student.objects.all().get(id=assistant_leader2)
        else:
            assistant_leader2=None
            
        if assistant_leader3!=None and assistant_leader3!='0' and assistant_leader3!=0 and assistant_leader3!='':
            assistant_leader3=Student.objects.all().get(id=assistant_leader3)
        else:
            assistant_leader3=None
        print('456')    
        if nid == None or nid == '' or nid == '0' or nid == 0:
            print('create')
            obj = Class_Group.objects.create(
                name=request.POST.get('name'),
                class_of_group=class_of_group,
                leader=leader,
                assistant_leader1=assistant_leader1,
                assistant_leader2=assistant_leader2,
                assistant_leader3=assistant_leader3,
                )
        else: #Update new class
            obj = Class_Group.objects.filter(id=str(nid)).update(
                name=request.POST.get('name'),
                class_of_group=class_of_group,
                leader=leader,
                assistant_leader1=assistant_leader1,
                assistant_leader2=assistant_leader2,
                assistant_leader3=assistant_leader3,
                )

    except Exception as e:
        print(e)
        response['message'] = '用戶輸入錯誤'
        if 'UNIQUE constraint' in str(e):
            response['message'] = '重複組別名稱'
        response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

@login_required(login_url='/admin/login')
def form_present_check(request):
    response = {'status':True,'message': None,'data':None}
    class_to_query = request.GET.get('class_to_query')
    print(class_to_query)
    try:
        if class_to_query!=None and class_to_query!='0' and class_to_query!=0 and class_to_query!='':
            classes=Class.objects.all().get(id=class_to_query)
        else:
            classes=None
    except Exception as e:
        print(e)
        response['message'] = '用戶輸入錯誤'
        if 'UNIQUE constraint' in str(e):
            response['message'] = '重複組別名稱'
        response['status'] = False

    context = {
        'class_to_query': Class.objects.all(),
        'class_i': classes,
    }
    return render(request, 'form_present_check.html', context=context)
    
@login_required(login_url='/admin/login')
def form_makeup_class(request):
    response = {'status':True,'message': None,'data':None}
    class_to_query = request.GET.get('class_to_query')
    name_to_query = request.GET.get('name')
    today = date.today()
    next_date = date.today()
    period_of_time = ['09:00', '11:00', '13:00', '15:00', '19:00']
    makeup_date_list = []
    max_slot_for_each_time = 5
    #create record in database
    #for period_of_time_i in period_of_time:
    #    try:
    #        MakeUpClassBookingRecord.objects.create(make_up_date=today,make_up_time=period_of_time_i)
    #    except Exception as e:
    #        pass
    try:
        if class_to_query!=None and class_to_query!='0' and class_to_query!=0 and class_to_query!='':
            classes=Class.objects.all().get(id=class_to_query)
            student_class_schedule=Student_Class_Schedule.objects.filter(class_of_student=class_to_query)
            student_class_schedule=list(filter(lambda x: (x.scheduled_class.study_time < today) & (x.present_check == False) & ((name_to_query in x.student.name) if name_to_query is not '' else True), student_class_schedule))
        else:
            classes=None
            student_class_schedule=None
    except Exception as e:
        response['message'] = '用戶輸入錯誤'
        if 'UNIQUE constraint' in str(e):
            response['message'] = '重複組別名稱'
        response['status'] = False
    #active_class = list(filter(lambda x: (x.class_of_student.year == today.year), Student_Class_Schedule.objects.all()))

    next_date = date.today() + relativedelta(months=+1)
    makeup_class_booking_record = list(filter(lambda x: (x.make_up_date.month == today.month) or (x.make_up_date.month == next_date.month), MakeUpClassBookingRecord.objects.all()))
    
    next_date = date.today()
    while True:
        next_date += timedelta(days=1)
        if next_date.month != today.month and next_date.day == 11:
            break
        date_with_record = []
        date_with_record.append(next_date)
        for period_of_time_i in period_of_time:
            exist_in_database = False
            for makeup_class_booking_record_i in makeup_class_booking_record:
                if next_date == makeup_class_booking_record_i.make_up_date and period_of_time_i == makeup_class_booking_record_i.make_up_time:
                    if makeup_class_booking_record_i.booking_record < max_slot_for_each_time:
                        date_with_record.append(makeup_class_booking_record_i.booking_record)
                    else:
                        date_with_record.append('滿')
                    exist_in_database = True
            if exist_in_database == False:
                date_with_record.append(0)
                
        makeup_date_list.append(date_with_record)
    context = {
        'class_to_query': Class.objects.all(),
        'class_i': classes,
        'student_class_schedule': student_class_schedule,
        'period_of_time': period_of_time,
        'makeup_date_list': makeup_date_list,
        'max_slot_for_each_time': max_slot_for_each_time,
    }
    return render(request, 'form_makeup_class.html', context=context)
    
@login_required(login_url='/admin/login')
def apply_for_make_up_class(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    student = Student.objects.filter(id=request.POST.get('student'))[0]
    make_up_date = request.POST.get('date')
    period_of_time = request.POST.get('period_of_time')
    student_class_schedule_nid = Student_Class_Schedule.objects.filter(id=nid)[0]
    
    #criteria to apply makr-up class
    if Student_Class_Schedule.objects.filter(student=student, make_up_date=make_up_date).count() >= 2:
        response['status'] = False
        response['message'] = '同一天不能補兩堂課'
    elif datetime.strptime(make_up_date, '%Y-%m-%d').date() <= (student_class_schedule_nid.scheduled_class.study_time + timedelta(days=2)):
        response['status'] = False
        response['message'] = '上課兩天後才能補課'
    else:
        try:
            MakeUpClassBookingRecord.objects.create(make_up_date=make_up_date, make_up_time=period_of_time, booking_record=1)
        except Exception as e:
            if 'UNIQUE constraint' in str(e):
                makeup_class_booking_record_obj = MakeUpClassBookingRecord.objects.filter(make_up_date=make_up_date, make_up_time=period_of_time)
                MakeUpClassBookingRecord.objects.filter(id=makeup_class_booking_record_obj[0].id).update(booking_record=(makeup_class_booking_record_obj[0].booking_record + 1))
        
        try:
            Student_Class_Schedule.objects.filter(id=nid).update(make_up_date=make_up_date, make_up_time=period_of_time)
        except Exception as e:
            print(e)
            response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)
    
@login_required(login_url='/admin/login')
def cancel_make_up_class(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    make_up_date = request.POST.get('date')
    period_of_time = request.POST.get('period_of_time')
    print(period_of_time)
    print(make_up_date)
    print(nid)
    try:
        makeup_class_booking_record_obj = MakeUpClassBookingRecord.objects.filter(make_up_date=make_up_date, make_up_time=period_of_time)
        print(makeup_class_booking_record_obj[0].booking_record)
        MakeUpClassBookingRecord.objects.filter(id=makeup_class_booking_record_obj[0].id).update(booking_record=(makeup_class_booking_record_obj[0].booking_record - 1))
    except Exception as e:
        response['status'] = False
    try:
        Student_Class_Schedule.objects.filter(id=nid).update(make_up_date=None, make_up_time='')
    except Exception as e:
        print(e)
        response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

@login_required(login_url='/admin/login')
def makeup_class_check_update(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    if request.POST.get('make_up_class') == 'true':
        make_up_class = True
    else:
        print('false')
        make_up_class = False
    try:
        if nid != '' or nid != '0' or nid != 0:
            obj = Student_Class_Schedule.objects.filter(id=nid).update(
                make_up_class=make_up_class,
                )
            response['nid'] = nid
        

    except Exception as e:
        print(e)
        response['message'] = '用戶輸入錯誤'
        response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)
    
@login_required(login_url='/admin/login')
def present_check_update(request):
    response = {'status':True,'message': None,'data':None}
    nid = request.POST.get('nid')
    if request.POST.get('present_check') == 'true':
        present_check = True
    else:
        present_check = False
    try:
        if nid != '' or nid != '0' or nid != 0:
            obj = Student_Class_Schedule.objects.filter(id=nid).update(
                present_check=present_check,
                )
            response['nid'] = nid
        

    except Exception as e:
        print(e)
        response['message'] = '用戶輸入錯誤'
        response['status'] = False

    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)
@login_required(login_url='/admin/login')
def check_in_qrcode(request):
    return render(request, 'check_in_qrcode.html')

@login_required(login_url='/admin/login')
def name_card_pdf(request, id):
    two_student_list = []
    class two_student:
        first_std_name = ""
        first_std_class = ""
        first_std_group = ""
        first_std_qr = ""
        second_std_name = ""
        second_std_class = ""
        second_std_group = ""
        second_std_qr = ""
    student_class = Student_Class.objects.all().filter(class_of_student=id)
    for n in range(len(student_class)):
        mod = n % 2
        student = two_student()
        if mod == 0:
            print(student_class[n].student.name)
            student.first_std_name = student_class[n].student.name
            student.first_std_class = student_class[n].class_of_student.name
            if student_class[n].group_of_student!= None: student.first_std_group = student_class[n].group_of_student.name
            student.first_std_qr = student_class[n].student_qr_code
            print(student.first_std_qr)
            if (n + 1) < len(student_class):
                print(student_class[n + 1].student.name)
                student.second_std_name = student_class[n + 1].student.name
                student.second_std_class = student_class[n + 1].class_of_student.name
                if student_class[n].group_of_student!= None: student.second_std_group = student_class[n + 1].group_of_student.name
                student.second_std_qr = student_class[n + 1].student_qr_code
                print(student.second_std_qr)
            print('-----')
            two_student_list.append(student)
        else:
            pass

    context = {
        'student_class': student_class,
        'two_student_list': two_student_list,
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
