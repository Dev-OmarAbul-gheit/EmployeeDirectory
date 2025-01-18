from rest_framework.viewsets import ModelViewSet
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
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
    def get_serializer_context(self):
        return {'request': self.request}