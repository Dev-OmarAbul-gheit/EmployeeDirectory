from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from . import views

router = DefaultRouter()
router.register('employees', viewset=views.EmployeeViewSet, basename='employee')
router.register('departments', viewset= views.DepartmentViewSet, basename='department')

departments_router = NestedDefaultRouter(router, 'departments', lookup='department')
departments_router.register('employees', viewset=views.EmployeeViewSet, basename='department-employee')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(departments_router.urls)),
]