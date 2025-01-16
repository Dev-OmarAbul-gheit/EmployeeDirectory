from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'gender', 'address', 'phone_number', 'email', 'department', 'salary']


class DepartmentSerializer(serializers.ModelSerializer):
    employees = serializers.HyperlinkedIdentityField(
        view_name = 'department-employee-list',
        read_only=True
    )
    class Meta:
        model = Department
        fields = ['id', 'name', 'employees']