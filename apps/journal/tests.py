from django.test import TestCase
from apps.catalog.models import Group, Subject, Teacher, Student
from .models import Lesson, Grade

class JournalTestCase(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name="Тест-Группа")
        self.subject = Subject.objects.create(name="Тест-Предмет")
        self.teacher = Teacher.objects.create(last_name="Иванов", first_name="Иван")
        self.student = Student.objects.create(group=self.group, last_name="Петров", first_name="Петр")
        self.lesson = Lesson.objects.create(date="2026-11-10", subject=self.subject, teacher=self.teacher)

    def test_grade_creation(self):
        grade = Grade.objects.create(lesson=self.lesson, student=self.student, value=5)
        self.assertEqual(grade.value, 5)
        self.assertEqual(grade.student.last_name, "Петров")