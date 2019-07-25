from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True, verbose_name='學員編號')
    name = models.CharField(max_length=60, default='', verbose_name='姓名')
    clerical_name = models.CharField(max_length=60, default='', blank=True, verbose_name='法名')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='出生日期')
    national_id_num = models.CharField(max_length=20, default='', blank=True, verbose_name='統一編號')
    phone_num = models.CharField(max_length=20, default='', verbose_name='電話')
    address = models.CharField(max_length=100, default='', blank=True, verbose_name='地址')
    invite_person = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='invite_person_set', blank=True, verbose_name='介紹人')
    emergency_contact_person = models.CharField(max_length=60, default='', blank=True, verbose_name='緊急聯絡人')
    emergency_contact_phone = models.CharField(max_length=20, default='', blank=True, verbose_name='緊急聯絡電話')
    #create_at = models.DateTimeField()
    def list_classes(self):
        return "\n".join(str(c.name + ':' + c.status.status) for c in self.class_of_student.all())
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "學員"
