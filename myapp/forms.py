from django.forms import ModelForm
from .models import UsersInfo,Student,Faculty

class UsersInfoForm(ModelForm):
    class Meta:
        model = UsersInfo
        fields = ['login_id', 'password','type']

class StudentFrom(ModelForm):
    class Meta:
        model = Student
        fields=['stu_id','login_id','stu_dept','stu_mail','stu_name','stu_level']

class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields=['fac_id','login_id','fac_name','fac_mail','fac_phone_no']
