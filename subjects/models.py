from django.db import models

from students.models import Student
from teachers.models import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=50)
    subject_day = models.CharField(max_length=50)
    start = models.TimeField()
    end = models.TimeField()
    teacher = models.ForeignKey(
        Teacher,
        related_name='subjects',
        on_delete=models.SET_NULL,
        null=True
    )
    students = models.ManyToManyField(Student, related_name='subjects')

    def __str__(self):
        return self.name
