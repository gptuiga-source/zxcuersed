from rest_framework import serializers
from .models import Lesson, Grade
from apps.catalog.models import Student

class GradeSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='lesson.subject.name', read_only=True)
    student_name = serializers.CharField(source='student.__str__', read_only=True)

    class Meta:
        model = Grade
        fields = ['id', 'lesson', 'student', 'student_name', 'subject_name', 'value', 'comment', 'created_at']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'