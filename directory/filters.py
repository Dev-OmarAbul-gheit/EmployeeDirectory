from django_filters.rest_framework import FilterSet
from .models import Employee

class EmployeeFilter(FilterSet):
    class Meta:
        model = Employee
        fields = {
            'department_id' : ['exact'],
            'salary' : ['gt', 'lt']
        }