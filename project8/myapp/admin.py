from django.contrib import admin

from myapp.models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','dob','email','usn','dept','college']

admin.site.register(Student,StudentAdmin)

