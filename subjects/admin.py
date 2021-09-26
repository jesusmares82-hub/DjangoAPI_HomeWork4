from django.contrib import admin

from students.models import Student
from subjects.models import Subject
from teachers.models import Teacher

admin.site.register(Student),
admin.site.register(Subject),
admin.site.register(Teacher)
