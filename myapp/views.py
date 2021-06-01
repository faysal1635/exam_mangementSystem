from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from operator import itemgetter
from django.db import IntegrityError,connection
from .models import Student,Admin,Faculty,UsersInfo
from .forms import UsersInfoForm,StudentFrom,FacultyForm
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'myapp/signupuser.html',{'form':UsersInfoForm()})
    else:
       if request.POST['password1'] == request.POST['password2']:
           newuser = UsersInfo()

           newuser.login_id = request.POST['login_id']
           newuser.password = request.POST['password1']
           newuser.type = request.POST['type']
           id=request.POST['login_id']
           res=UsersInfo.objects.filter(login_id__exact=str(id))
           print(res)
           for i in res:
                if  res[0]=="":
                    newuser.save()
                else:
                   return render(request, 'myapp/signupuser.html',{'form':UsersInfoForm(),'error':'please choose a new login_id'})            #didnt match

           if request.POST['type']== 'student':
                newuser.save()
                return redirect('student_views')
           elif request.POST['type']== 'faculty':
                newuser.save()
                return redirect('faculty_views')
           elif request.POST['type']== 'admin':
                newuser.save()
                return redirect('admin_views')
           else:
               return render(request, 'myapp/signupuser.html',{'form':UsersInfoForm(),'error':'Invalid type'})            #didnt match



       else:
          return render(request, 'myapp/signupuser.html',{'form':UsersInfoForm(),'error':'password did not match'})            #didnt match

    #else:
    #    if request.POST['password1'] == request.POST['password2']:
    #        try:
                #form = UsersInfoForm(request.POST)
                #newuser = form.save(commit=False)
                #newuser.user = request.user
                #newuser.save()
                #if request.POST['type']== 'student':
                #    return redirect('student_views')
            #    else:
            #        return redirect('faculty_views')
#
            #except IntegrityError:
            #    return render(request, 'myapp/signupuser.html',{'form':UsersInfoForm(),'error':'please choose a new one'})            #didnt match
        #else:
        #    return render(request, 'myapp/signupuser.html',{'form':UsersInfoForm(),'error':'password did not match'})            #didnt match


def signinuser(request):
    if request.method == 'GET':
        return render(request,'myapp/signinuser.html')
    else:
        cursor =connection.cursor()
        cursor =connection.cursor()
        #sql = "select login_id form myapp_UserInfo"
        #sql2 = "select password form myapp_UserInfo"
        cursor.execute("select login_id,password,type from users_info")
        e=[]
        for i in cursor:
            e.append(i)
        cursor.execute("select password from users_info")
        p=[]
        for i in cursor:
            p.append(i)
        res = list(map(itemgetter(0),e))
        res2 = list(map(itemgetter(0),p))
        res3 = list(map(itemgetter(2),e))

        id=request.POST['login_id']
        password=request.POST['password']
        type=request.POST['type']
        print(e)
        print(p)
        print(res)
        print(res3)
        print(res[0])
        print(str(id))
        print(res2[0])
        print(str(password))

        j=0
        k=len(res)
        while j<k:
            if res[j]==str(id) and res2[j]==str(password):
                print(res[j])
                if str(type)==res3[j]:
                    if str(type)=='student':
                        return redirect('student')
                    elif str(type)=='faculty':
                        return redirect('faculty')
                    else:
                        return render(request,'myapp/signinuser.html',{'error':'Type did not match'})
                        break
                else:
                    return render(request,'myapp/signinuser.html',{'error':'Type did not match'})
            else:
                j=j+1
        else:
            return render(request, 'myapp/signinuser.html',{'form':UsersInfoForm(),'error':'Login_id and password did not match'})

                #didnt match


    return render(request,'myapp/signinuser.html')

def student_views(request):
    if request.method == 'GET':
        return render(request,'myapp/student_views.html',{'form':StudentFrom()})
    else:
         user = Student()

         user.stu_id = request.POST['stu_id']
         user.login_id = request.POST['login_id']
         user.stu_name = request.POST['stu_name']
         user.stu_dept = request.POST['stu_dept']
         user.stu_level = request.POST['stu_level']
         user.stu_mail = request.POST['stu_mail']
         id=request.POST['login_id']
         res=Student.objects.filter(login_id__exact=str(id))
         sid=request.POST['stu_id']
         sres=Student.objects.filter(stu_id__exact=str(sid))

         for i in res:
                if res[0]!="":
                    return render(request, 'myapp/student_views.html',{'form':StudentFrom(),'error':'Login ID is already used '})            #didnt match
                else:
                    pass
    for j in sres:
            if sres[0]!="":
                return render(request, 'myapp/student_views.html',{'form':StudentFrom(),'error':'Student ID is already used '})            #didnt match
            else:
                pass
    user.save()
    return redirect('student')

def faculty_views(request):
    if request.method == 'GET':
        return render(request,'myapp/faculty_views.html',{'form':FacultyForm()})
    else:
         user = Faculty()

         user.fac_id = request.POST['fac_id']
         user.login_id = request.POST['login_id']
         user.fac_name = request.POST['fac_name']
         user.fac_phone_no = request.POST['fac_phone_no']
         user.fac_mail = request.POST['fac_mail']
         id=request.POST['login_id']
         res=Faculty.objects.filter(login_id__exact=str(id))
         sid=request.POST['fac_id']
         sres=Faculty.objects.filter(fac_id__exact=str(sid))

         for i in res:
                if res[0]!="":
                    return render(request, 'myapp/faculty_views.html',{'form':FacultyForm(),'error':'Login ID is already used '})            #didnt match
                else:
                    pass
    for j in sres:
            if sres[0]!="":
                return render(request, 'myapp/faculty_views.html',{'form':FacultyForm(),'error':'Student ID is already used '})            #didnt match
            else:
                pass
    user.save()
    return redirect('faculty')

def admin_views(request):
    return render(request,'myapp/admin_views.html')
def student(request):
    return render(request,'myapp/student.html')
def faculty(request):
    return render(request,'myapp/faculty.html')
def admin(request):
    return render(request,'myapp/admin.html')
