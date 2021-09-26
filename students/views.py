from copy import copy

from django.core.exceptions import FieldError
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from students.models import Student
from students.serializers import StudentSerializer


class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        data = copy(request.data)
        print(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_mail(
            subject='Bienvenido a Academlo',
            message='Nos complace darte la bienvenida: ' + data.get('name'),
            html_message='<h1>Nos complace darte la bienvenida: ' + data.get('name') + '</h1>',
            from_email='hola@academlo.com',
            recipient_list=['user@gmail.com']
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

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
