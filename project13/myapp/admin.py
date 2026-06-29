from django.contrib import admin
from myapp.models import Student, Teacher


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sem1', 'sem2', 'sem3', 'sem4', 'sem5', 'sem6', 'sem7', 'sem8')
    search_fields = ('name',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
