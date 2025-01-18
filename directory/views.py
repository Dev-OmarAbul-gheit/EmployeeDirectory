from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeList(APIView):
    def get(self, request, pk=None):
        queryset = Employee.objects.all()
        if pk:
            queryset = queryset.filter(department_id = pk)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, pk=None):
        context = {}
        if pk:
            context = {'department_id' : pk}
        serializer = EmployeeSerializer(data=request.data, context =context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EmployeeDetail(APIView):
    def get(self, request, pk=None, emp_pk=None):
        employee = get_object_or_404(Employee, pk=emp_pk, department_id = pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def patch(self,request, pk=None, emp_pk=None):
        employee = get_object_or_404(Employee, pk=emp_pk, department_id = pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=None, emp_pk=None):
        employee = get_object_or_404(Employee, pk=emp_pk, department_id = pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentList(APIView):
    def get(self, request):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data, context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DepartmentDetail(APIView):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department, context = {'request': request})
        return Response(serializer.data)

    def patch(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department, data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)