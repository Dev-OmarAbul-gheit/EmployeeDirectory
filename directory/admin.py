from django.contrib import admin, messages
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