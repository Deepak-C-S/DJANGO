from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'place', 'job', 'salary')

admin.site.register(Employee, EmployeeAdmin)