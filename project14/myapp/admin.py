from django.contrib import admin
from myapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'email', 'college', 'cgpa')

admin.site.register(Student, StudentAdmin)

    