from django.contrib import admin
from myapp.models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email')

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
