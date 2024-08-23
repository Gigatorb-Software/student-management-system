from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from django.contrib import messages
from . models import Registration, Course, AddStudents, Teacher
from django.contrib import auth

# Create your views here.


def index(request):
    return render(request, 'index.html')


def courses(request):
    data = Course.objects.all()
    return render(request, 'courses.html', {"data": data})


def dashboard(request):
    data = Course.objects.all()
    c = Course.objects.all().count()
    a = AddStudents.objects.all().count()
    t = Teacher.objects.all().count()
    return render(request, 'dashboard.html', {'c': c, 'a': a, 't': t, 'data': data})


def employees(request):
    return render(request, 'employees.html')


def notifications(request):
    return render(request, 'notifications.html')


def pgdashboard(request):
    return render(request, 'pg_dashboard.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'sign-up.html')


def tables(request):
    return render(request, 'tables.html')


def tenants(request):
    return render(request, 'tenants.html')


def viewstudents(request):
    stu = AddStudents.objects.all()
    addcourses = Course.objects.all()
    redirect("/viewstudents/")
    return render(request, 'viewstudents.html', {'stu': stu, 'addcourses': addcourses})

# registration


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = make_password(request.POST['password'])
        if Registration.objects.filter(email=email).exists():
            messages.error(request, "email already exists")
            return redirect('/')
        elif Registration.objects.filter(contact=contact).exists():
            messages.error(request, "contact number already exists")
            return redirect('/')
        else:
            Registration.objects.create(
                name=name, email=email, password=password, contact=contact)
            return redirect('/')


# login
def login(request):
    if request.method == "POST":
        contact = request.POST['contact']
        password = request.POST['password']
        if Registration.objects.filter(contact=contact).exists():
            inst = Registration.objects.get(contact=contact)
            psw = inst.password
            if check_password(password, psw):
                return redirect('/dashboard/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse("phone number is not registered")


# add course


def addcourse(request):
    if request.method == 'POST':
        name = request.POST['course']
        fees = request.POST['fees']
        duration = request.POST['duration']
        comments = request.POST['comment']
        if Course.objects.filter(name=name).exists():
            messages.error(request, "already exists")
            data = Course.objects.all()
            return render(request, 'courses.html', {'data': data})
        else:
            Course.objects.create(name=name, fees=fees,
                                  duration=duration, comments=comments)
            data = Course.objects.all()
            return render(request, 'courses.html', {'data': data})
    else:
        return render(request, 'courses.html', {'data': data})


# delete course

def delete(request, pk):
    Course.objects.filter(id=pk).delete()
    return redirect('/courses/')

 # update course


def update_view(request, uid):
    res = Course.objects.get(id=uid)
    return render(request, 'updatecourse.html', {'course': res, })


def updatecourse(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        name = request.POST['course']
        fees = request.POST['fees']
        duration = request.POST['duration']
        comments = request.POST['comment']
        Course.objects.filter(id=uid).update(
            name=name, fees=fees, duration=duration, comments=comments)
        return redirect('/courses/')


# add student
def addstudent(request):
    if request.method == "POST":
        stu_name = request.POST.get("Name")
        stu_email = request.POST.get("Email")
        stu_mobile = request.POST.get("Mobile")
        stu_college = request.POST.get("College")
        stu_degree = request.POST.get("Degree")
        stu_address = request.POST.get("Address")
        stu_addcourse_id = request.POST.get("course")
        total_amount = request.POST.get("qty")
        paid_amount = request.POST.get("cost")
        due_amount = request.POST.get("DueAmount")
        stu_course = Course.objects.get(id=stu_addcourse_id)
        if AddStudents.objects.filter(semail=stu_email).exists():
            messages.error(request, "Email id already exists")
            return redirect("/addstudent/")

        elif AddStudents.objects.filter(smobile=stu_mobile).exists():
            messages.error(request, "Mobile Number already exists")
            return redirect("/addstudent/")
        else:
            AddStudents.objects.create(sname=stu_name,
                                       semail=stu_email,
                                       smobile=stu_mobile,
                                       scollege=stu_college,
                                       sdegree=stu_degree,
                                       saddress=stu_address,
                                       scourse=stu_course,
                                       total_amount=total_amount,
                                       paid_amount=paid_amount,
                                       due_amount=due_amount,
                                       )
            messages.success(request, "Student Added Successfully!!")
            stu = AddStudents.objects.all()
            addcourses = Course.objects.all()
            return render(request, 'viewstudents.html', {'stu': stu, 'addcourses': addcourses,
                                                         })
    else:
        stu = AddStudents.objects.all()
        addcourses = Course.objects.all()
        return render(request, 'viewstudents.html', {'stu': stu, 'addcourses': addcourses})


def updatestu(request, uid):
    res = AddStudents.objects.get(id=uid)
    addcourses = Course.objects.all()

    return render(request, 'updatestudent.html', {'stu': res, 'addcourses': addcourses})


def update_student(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        sname = request.POST['name']
        semail = request.POST['email']
        smobile = request.POST['mobile']
        sdegree = request.POST['degree']
        scourse = request.POST['course']
        AddStudents.objects.filter(id=uid).update(sname=sname, semail=semail,
                                                  smobile=smobile, sdegree=sdegree,
                                                  scourse=scourse
                                                  )
        return redirect('/viewstudents/')


def teacher(request):
    tech = Teacher.objects.all()
    addcourses = Course.objects.all()
    redirect('/teacher/')
    return render(request, 'teacher.html',  {'tech': tech, 'addcourses': addcourses})


def addteacher(request):
    if request.method == 'POST':
        tech_name = request.POST.get("name")
        tech_employeesid = request.POST.get("employeesid")
        tech_email = request.POST.get("email")
        tech_password = make_password(request.POST.get("password"))
        tech_contact = request.POST.get("mobile")
        tech_joindate = request.POST.get("joindate")
        tech_education = request.POST.get("education")
        tech_workexp = request.POST.get("workexp")
        tech_addcourse_id = request.POST.get("course")
        tech_gender = request.POST.get("radio")
        photo = request.FILES.get('photo')
        tech_course = Course.objects.get(id=tech_addcourse_id)
        if Teacher.objects.filter(teacheremail=tech_email).exists():
            messages.error(request, "Email id already exists")
            return redirect("/addteacher/")

        elif Teacher.objects.filter(teachermobile=tech_contact).exists():
            messages.error(request, "mobile Number already exists")
            return redirect("/addteacher/")
        else:
            Teacher.objects.create(teachername=tech_name,
                                   employeesid=tech_employeesid,
                                   teacheremail=tech_email,
                                   teacherpassword=tech_password,
                                   teachermobile=tech_contact,
                                   joindate=tech_joindate,
                                   education=tech_education,
                                   workexp=tech_workexp,
                                   teachercourse=tech_course,
                                   gender=tech_gender,
                                   photo=photo)
            messages.success(request, "teacher added successfully")
            tech = Teacher.objects.all()
            addcourses = Course.objects.all()
            return render(request, 'teacher.html', {'tech': tech, 'addcourses': addcourses})
    else:
        tech = Teacher.objects.all()
        addcourses = Course.objects.all()
        return render(request, 'teacher.html', {'tech': tech, 'addcourses': addcourses})


def updatetech(request, uid):
    res = Teacher.objects.get(id=uid)
    addcourses = Course.objects.all()

    return render(request, 'update_tech.html', {'i': res, 'addcourses': addcourses})


def update_teacher(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        teachername = request.POST['name']
        employeesid = request.POST['employeesid']
        teacheremail = request.POST['email']
        teachermobile = request.POST['mobile']
        workexp = request.POST['workexp']
        education = request.POST['education']
        joindate = request.POST['joindate']
        Teacher.objects.filter(id=uid).update(teachername=teachername, employeesid=employeesid,
                                              teacheremail=teacheremail,
                                              teachermobile=teachermobile, workexp=workexp,
                                              education=education,
                                              joindate=joindate,
                                              )
        return redirect('/teacher/')


def logout(request):
    auth.logout(request)
    messages.warning(request, 'sucessfully logout')
    return redirect('/')
