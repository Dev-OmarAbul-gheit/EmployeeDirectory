from django.urls import path
from . import views

urlpatterns = [
    path('employees/', view=views.employee_list, name='employee-list'),
    path('employees/<int:pk>', view=views.employee_detail, name='employee-detail'),
    path('departments/', view=views.department_list, name='department-list'),
    path('departments/<int:pk>', view=views.department_detail, name='department-detail'),
    path('departments/<int:pk>/employees', view=views.department_employee_list, name='department-employee-list'),
    path('departments/<int:pk>/employees/<int:emp_pk>', view=views.department_employee_detail, name='department-employee-detail')
]