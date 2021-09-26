from rest_framework.serializers import ModelSerializer

from subjects.models import Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


"""class StudentDetailSerializer(ModelSerializer):
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'"""


class CreateSubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
