from django.urls import path
from . import views

urlpatterns = [
    path('employees/', view=views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', view=views.EmployeeDetail.as_view(), name='employee-detail'),
    path('departments/', view=views.DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>/', view=views.DepartmentDetail.as_view(), name='department-detail'),
    path('departments/<int:pk>/employees/', view=views.EmployeeList.as_view(), name='department-employee-list'),
    path('departments/<int:pk>/employees/<int:emp_pk>/', view=views.EmployeeDetail.as_view(), name='department-employee-detail')
]