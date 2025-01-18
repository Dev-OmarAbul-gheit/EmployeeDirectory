from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeList(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        department_id = self.request.parser_context['kwargs'].get('pk')
        if department_id:
            return Employee.objects.filter(department_id=department_id)
        return Employee.objects.all()

    def get_serializer_context(self):
        context = {}
        department_id = self.request.parser_context['kwargs'].get('pk')
        if department_id:
            context = {'department_id' : department_id}
        return context

class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    
    def get_object(self):
        pk1 = self.request.parser_context['kwargs'].get('pk')
        pk2 = self.request.parser_context['kwargs'].get('emp_pk')
        if pk2:
            return get_object_or_404(Employee, pk=pk2, department_id=pk1)
        else:
            return get_object_or_404(Employee, pk=pk1)


class DepartmentList(ListCreateAPIView):
    queryset = Department.objects.prefetch_related('employees').all()
    serializer_class = DepartmentSerializer
    def get_serializer_context(self):
        return {'request': self.request}


class DepartmentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.prefetch_related('employees').all()
    serializer_class = DepartmentSerializer
    def get_serializer_context(self):
        return {'request': self.request}