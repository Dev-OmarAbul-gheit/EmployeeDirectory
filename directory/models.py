from django.db import models
from django.core.validators import MinValueValidator

class Employee(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default= GENDER_MALE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='employees')
    salary = models.PositiveIntegerField(validators=[MinValueValidator(3000)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['first_name', 'last_name']

class Department(models.Model):
    name = models.CharField(max_length=255)

    @property
    def employees_count(self):
        return self.employees.count()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name