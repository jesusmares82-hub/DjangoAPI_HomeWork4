from django.core.exceptions import ObjectDoesNotExist, FieldError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from students.models import Student
from students.serializers import StudentSerializer
from subjects.models import Subject
from subjects.serializers import SubjectSerializer


class SubjectViewset(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    @action(methods=['GET', 'POST'], detail=True)
    def students(self, request, pk):
        subject = Subject.objects.get(id=pk)

        if request.method == 'GET':
            students = subject.students.all()
            serialized = StudentSerializer(students, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

        if request.method == 'POST':
            ids_students = request.data.get('students', [])
            invalid_ids = []
            for ID in ids_students:
                try:
                    student = Student.objects.get(id=ID)
                    subject.students.add(student)
                except ObjectDoesNotExist:
                    invalid_ids.append(ID)
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'invalid_ids': invalid_ids,
                    'data': SubjectSerializer(subject).data}
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
