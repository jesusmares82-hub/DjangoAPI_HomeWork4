from rest_framework.serializers import ModelSerializer

from teachers.models import Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


"""class StudentDetailSerializer(ModelSerializer):
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'"""


class CreateTeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
