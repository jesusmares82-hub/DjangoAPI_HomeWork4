from django.core.exceptions import FieldError
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from teachers.models import Teacher
from teachers.serializer import TeacherSerializer


class TeacherViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @action(methods=['GET'], detail=False)
    def get_queryset(self):
        param_filter = {}
        for param in self.request.query_params:
            if not param.startswith('name'):
                continue
            param_filter[param] = self.request.query_params[param]
        try:
            return self.queryset.filter(**param_filter)
        except FieldError:
            return self.queryset
