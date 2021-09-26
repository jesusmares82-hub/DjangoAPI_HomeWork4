from rest_framework.serializers import ModelSerializer

from students.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


"""class StudentDetailSerializer(ModelSerializer):
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'"""


class CreateStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
