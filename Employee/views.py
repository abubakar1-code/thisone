from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import (Department,
                     Employee,
                    Project,
                    WorkOn
                     )

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request,'index.html',{})

def admin_login(request):
    return redirect('/admin')


@user_passes_test(lambda u: u.is_superuser)
def departments(request):

    if request.user.is_authenticated:
        authorusername  = str(request.user.username)
        departments = Department.objects.all()
        department_list = []
        len_e = len(departments)
        for it in departments:
            department_list.append((it.name,it.number))

        return render(request,'departments.html',context=
                                  {'authorusername':authorusername,
                                   'departments':departments,
                                   'len':len_e
                                   }
                                  )

@user_passes_test(lambda u: u.is_superuser)
def projects(request):
    if request.user.is_authenticated:
        authorusername  = str(request.user.username)
        projects = Project.objects.all()
        project_list = []
        len_e = len(projects)
        for it in projects:
            project_list.append((it.name,it.number))

        return render(request,'projects.html',context=
                                  {'authorusername':authorusername,
                                   'projects':projects,
                                   'len':len_e
                                   }
                                  )

@user_passes_test(lambda u: u.is_superuser)
def employees(request):

    if request.user.is_authenticated:
        authorusername  = str(request.user.username)
        employees = Employee.objects.all()
        project_list = []
        len_e = len(employees)
        for it in range(len(employees)):
            temp1  = employees[it].project.all()
            for item3 in temp1:
                project_list.append((item3.name,employees[it].number))
        return render(request,'employees.html',context=
                                  {'authorusername':authorusername,
                                   'employees':employees,
                                   'len':len_e,'project_list':project_list
                                   }
                                  )

@user_passes_test(lambda u: u.is_superuser)
def employeedetail(request,query):
    if request.user.is_authenticated:
        authorusername  = str(request.user.username)
        employee = Employee.objects.filter(number=query).get()
        project_list = employee.project.all()
        return render(request,'employeedetail.html',
                                  {'authorusername': authorusername,
                                   'employee': employee,
                                    'project_list': project_list
                                   }

                                  )

@user_passes_test(lambda u: u.is_superuser)
def departmentdetail(request,query):
    if request.user.is_authenticated:
        authorusername = str(request.user.username)
        department  = Department.objects.filter(number=query).get()
        employee_count= Employee.objects.filter(department__pk=query).count()
        return render(request,'departmentdetail.html',
                                  {'authorusername': authorusername,
                                   'department': department,
                                   'employee_count': employee_count
                                   }
                                  )

@user_passes_test(lambda u: u.is_superuser)
def projectdetail(request,query):
    if request.user.is_authenticated:
        authorusername = str(request.user.username)
        project = Project.objects.filter(number=query).get()
        employee_count = Employee.objects.filter(department__name=project.name).count()
        return render(request,'projectdetail.html',
                                  {'authorusername': authorusername,
                                   'project': project,
                                   'employee_count': employee_count
                                   }
                                  )

