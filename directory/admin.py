from django.contrib import admin, messages
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode 
from .models import Employee, Department

admin.site.site_header = 'Employee Directory Admin'
admin.site.index_title = 'Admin'

class SalaryFilter(admin.SimpleListFilter):
    title = 'salary'
    parameter_name = 'salary'

    def lookups(self, request, model_admin):
        return [
            ('<10000', '<10000'),
            ('<30000', '<30000'),
            ('>30000', '>30000'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10000': 
            return queryset.filter(salary__lt=10000)
        elif self.value() == '<3000':
            return queryset.filter(salary__lt=30000)
        elif self.value() == '>30000':
            return queryset.filter(salary__gt = 30000)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'address', 'phone_number', 'email', 'department', 'salary']
    list_editable = ['address', 'phone_number', 'email', 'salary']
    list_per_page = 10
    list_filter = ['gender', 'department', SalaryFilter]
    search_fields = ['first_name__istartswith', 'last_name__istartswith', 'phone_number', 'email', 'address']
    actions = ['rasie_salary', 'deducte_salary']

    @admin.action(description='Rasie Salary')
    def rasie_salary(self, request, queryset):
        employee_count = queryset.count()
        for employee in queryset:
            employee.salary += (employee.salary * 0.1) 
            employee.save()

        self.message_user(
            request,
            f"{employee_count} employees have successfully got a salary rasie by 10%",
            messages.SUCCESS
        )

    @admin.action(description='Deducte Salary')
    def deducte_salary(self, request, queryset):
        employees_count = queryset.count()
        for employee in queryset:
            employee.salary -= (employee.salary * 0.1)
            employee.save()
        
        self.message_user(
            request,
            f"{employees_count} employees have got a salary deducte by 10%",
            messages.WARNING   
        )


class EmployeesCountFilter(admin.SimpleListFilter):
    title = 'team size'
    parameter_name = 'employees_count'

    def lookups(self, request, model_admin):
        return [
            ('small', 'Small Team'),
            ('big', 'Big Team'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'small': 
            return queryset.filter(employees_count__lt = 5)
        elif self.value() == 'big':
            return queryset.filter(employees_count__gt = 5)


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 0
    min_num = 1

@admin.register(Department)
class DepartmentModel(admin.ModelAdmin):
    inlines = [EmployeeInline]
    list_display = ['id', 'name', 'employees_count']
    list_editable = ['name']
    list_per_page = 10
    search_fields = ['name__istartswith']
    list_filter = ['name', EmployeesCountFilter]
    actions = ['remove_employees']

    @admin.display(ordering='employees_count')
    def employees_count(self, department):
        url = reverse('admin:directory_employee_changelist') \
              + '?' \
              + urlencode({'department__id': str(department.id)})

        return format_html(f'<a href="{url}">{department.employees_count}</a>')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            employees_count = Count('employees')
        )
    
    @admin.action(description= 'Remove all employees')
    def remove_employees(self, request, queryset):
        employees_count = 0
        departments = [department.name for department in list(queryset)]
        for department in queryset:
            employees_count += department.employees.count()
            department.employees.update(department_id = None)
        
        self.message_user(
            request,
            f"{employees_count} employees have removed from {departments} departments.",
            messages.WARNING   
        )