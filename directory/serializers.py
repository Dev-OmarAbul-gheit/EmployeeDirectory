from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'gender', 'address', 'phone_number', 'email', 'department', 'salary']

    def create(self, validated_data):
        department_id = self.context.get('department_id')
        if department_id:
            validated_data['department_id'] = department_id
        
        employee = Employee.objects.create(**validated_data)
        return employee


class DepartmentSerializer(serializers.ModelSerializer):
    employees = serializers.HyperlinkedIdentityField(
        view_name='department-employee-list',
        lookup_url_kwarg='department_pk',
    )
    employees_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ['id', 'name', 'employees', 'employees_count']

    def get_employees_count(self, department):
        return department.employees.count()