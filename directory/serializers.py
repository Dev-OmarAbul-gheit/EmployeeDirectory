from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'gender', 'address', 'phone_number', 'email', 'department', 'salary']


class DepartmentSerializer(serializers.ModelSerializer):
    employees = serializers.HyperlinkedIdentityField(
        view_name = 'department-employee-list'
    )
    class Meta:
        model = Department
        fields = ['id', 'name', 'employees']