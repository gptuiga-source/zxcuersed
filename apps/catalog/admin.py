from django.contrib import admin

from .models import Group, Student, Subject, Teacher


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name")
    search_fields = ("last_name", "first_name", "middle_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "group")
    list_filter = ("group",)
    search_fields = ("last_name", "first_name", "middle_name")
    autocomplete_fields = ("group",)


