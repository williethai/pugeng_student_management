from django import forms
from .models import *

        
class StudentForm(forms.ModelForm):
    classes = forms.ModelChoiceField(queryset=Class.objects.filter(id=1))
    class Meta:      
        model = Student
        fields = '__all__'