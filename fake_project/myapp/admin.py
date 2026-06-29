from django.contrib import admin
from .models import *
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'job', 'place', 'email')

admin.site.register(Employee, EmployeeAdmin)


