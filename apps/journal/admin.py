from django.contrib import admin
from .models import Lesson, Grade

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "subject", "teacher")
    list_filter = ("subject", "teacher")
    search_fields = ("topic", "subject__name", "teacher__last_name")
    autocomplete_fields = ("subject", "teacher")
    inlines = [GradeInline]

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "student", "value", "created_at")
    list_filter = ("value", "lesson__subject")
    search_fields = ("student__last_name", "student__first_name", "lesson__topic")
    autocomplete_fields = ("lesson", "student")
