from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PATCH', 'DELETE'])
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'GET':        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = EmployeeSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    queryset = Employee.objects.filter(department_id=pk)
    serializer = EmployeeSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def department_employee_detail(request, pk, emp_pk):
    employee = get_object_or_404(Employee, pk=emp_pk, department_id=pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)