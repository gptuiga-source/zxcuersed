from django.db import models                         # поля моделей


class Group(models.Model):
    name = models.CharField("Название группы", max_length=100, unique=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=150, unique=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    last_name = models.CharField("Фамилия", max_length=100)
    first_name = models.CharField("Имя", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100, blank=True)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ("last_name", "first_name")

    def __str__(self):
        return " ".join(part for part in (self.last_name, self.first_name, self.middle_name) if part)


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name="Группа")
    last_name = models.CharField("Фамилия", max_length=100)
    first_name = models.CharField("Имя", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100, blank=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ("last_name", "first_name")

    def __str__(self):
        full_name = " ".join(part for part in (self.last_name, self.first_name, self.middle_name) if part)
        return f"{full_name} ({self.group})"


class Location(models.Model):                        # модель «Локация»
    name = models.CharField("Название", max_length=255) # название, до 255 символов

    class Meta:                                      # мета-настройки
        verbose_name = "Локация"                     # имя в ед. числе
        verbose_name_plural = "Локации"              # имя во мн. числе

    def __str__(self):                               # как печатается объект
        return self.name                             # возвращаем название


class Category(models.Model):                        # модель «Категория»
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Vendor(models.Model):                          # модель «Производитель»
    name = models.CharField("Название", max_length=255, unique=True) # уникально

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name


class Model(models.Model):                           # модель «Модель оборудования»
    vendor = models.ForeignKey(                      # связь с производителем
        Vendor, on_delete=models.PROTECT,            # запрет удаления, если есть ссылки
        verbose_name="Производитель",
    )
    category = models.ForeignKey(                    # связь с категорией
        Category, on_delete=models.PROTECT,
        verbose_name="Категория",
    )
    name = models.CharField("Модель", max_length=255) # название модели

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return f"{self.vendor.name} {self.name}"     # например, «HP ProBook 450»
