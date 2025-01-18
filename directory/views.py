from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from .filters import EmployeeFilter


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = EmployeeFilter
    search_fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']
    def get_queryset(self):
        department_pk = self.kwargs.get('department_pk')
        if department_pk:
            return Employee.objects.filter(department_id = department_pk)
        return Employee.objects.all()
    
    def get_serializer_context(self):
        context = {}
        department_pk = self.kwargs.get('department_pk')
        if department_pk:
            context = {'department_id' : department_pk}
        return context


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.prefetch_related('employees').all()
    serializer_class = DepartmentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    def get_serializer_context(self):
        return {'request': self.request}