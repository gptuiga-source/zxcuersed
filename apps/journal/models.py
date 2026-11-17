from django.db import models
from apps.catalog.models import Student, Subject, Teacher

class Lesson(models.Model):
    date = models.DateField("Дата")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    topic = models.CharField("Тема урока", max_length=255, blank=True)
    
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - {self.subject.name}"

class Grade(models.Model):
    class GradeValue(models.IntegerChoices):
        TWO = 2, "2 (Неудовлетворительно)"
        THREE = 3, "3 (Удовлетворительно)"
        FOUR = 4, "4 (Хорошо)"
        FIVE = 5, "5 (Отлично)"

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    value = models.IntegerField("Оценка", choices=GradeValue.choices)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата выставления", auto_now_add=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        unique_together = ('lesson', 'student')  # Один студент - одна оценка за урок

    def __str__(self):
        return f"{self.student} - {self.value} ({self.lesson.subject.name})"