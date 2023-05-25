from django.db import models
from .utils import validate_phone_number

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=125, verbose_name="Название урока")

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="Firstame")
    lastname = models.CharField(max_length=50, verbose_name="Lastname")
    email = models.EmailField(max_length=80, verbose_name="Email", help_text="ali@gmai")
    # validators=validate_phone_number указывает валидацию метод
    phone = models.CharField(max_length=12, verbose_name="Phone number", validators=[validate_phone_number])
    adress = models.CharField(max_length=50, verbose_name="Adress lived")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name="Subject")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")

    @property
    def full_name(self):
        return self.firstname + " " + self.lastname

    def __str__(self) -> str:
        return self.lastname + " " + self.firstname + " | " + self.phone
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Klass(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Number Class")
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name="Teacher")

    def __str__(self) -> str:
        return f"Number class: {self.number} | {self.teacher}"
    
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Clases"


class Student(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="Firstame")
    lastname = models.CharField(max_length=50, verbose_name="Lastname")
    email = models.EmailField(max_length=80, verbose_name="Email", help_text="ali@gmai")
    phone = models.CharField(max_length=12, verbose_name="Phone number", validators=[validate_phone_number])
    adress = models.CharField(max_length=50, verbose_name="Adress lived")
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name="Teacher")

    @property
    def full_name(self):
        return self.firstname + " " + self.lastname

    def __str__(self) -> str:
        return self.lastname + " " + self.firstname + " | " + self.teacher.lastname + self.teacher.firstname
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"