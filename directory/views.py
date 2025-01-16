from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


@api_view()
def employee_list(request):
    queryset = Employee.objects.select_related('department')
    serializer = EmployeeSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def employee_detail(request, pk):
    employee = get_object_or_404(Employee.objects.select_related('department'), pk=pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

@api_view()
def department_list(request):
    queryset = Department.objects.prefetch_related('employees')
    serializer = DepartmentSerializer(queryset, many=True, context = {'request':request})
    return Response(serializer.data)

@api_view()
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    serilializer = DepartmentSerializer(department, context = {'request':request})
    return Response(serilializer.data)

@api_view()
def department_employee_list(request, pk):
    queryset = Employee.objects.select_related('department').filter(department_id=pk)
    serializer = EmployeeSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def department_employee_detail(request, pk, emp_pk):
    employee = get_object_or_404(Employee.objects.select_related('department'), pk=emp_pk, department_id=pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)