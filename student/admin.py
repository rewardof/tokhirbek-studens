from django.contrib import admin

from .models import Student, Course, Faculty, Teacher, Marks

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Faculty)
admin.site.register(Marks)
