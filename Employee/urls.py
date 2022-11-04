from django.urls import include, re_path
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
re_path(r'^$',views.home,name='home'),
re_path(r'^accounts/login/$',views.admin_login,name='admin_login'),
re_path(r'^employees/$',views.employees,name='employees'),
re_path(r'^departments/$',views.departments,name='departments'),
re_path(r'^projects/$',views.projects,name='projects'),
re_path(r'^employee/(?P<query>\w+)/$',views.employeedetail,name='employeedetail'),
re_path(r'^department/(?P<query>\w+)/$',views.departmentdetail,name='departmentdetail'),
re_path(r'^project/(?P<query>\w+)/$',views.projectdetail,name='projectdetail'),



    ]
