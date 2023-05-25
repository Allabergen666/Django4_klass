from django.contrib import admin
from .models import Subject, Teacher, Klass, Student

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    # list_display принисает tuple or list, Показывает по столбцам
    list_display = ['name',]
    search_fields = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # list_display принисает tuple or list, Показывает по столбцам
    list_display = ('full_name','email','phone','adress', 'subject', 'create_at')
    #  search_fields Поиск 
    search_fields = ('firstname','lastname', 'email','phone','adress', 'subject__name')
    # list_filter сортировать по курс, группа, факултатив
    list_filter = ('subject', 'create_at')
    

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    list_display = ('number', 'teacher')
    search_fields = ('number', 'teacher__firstname', 'teacher__lastname')
    list_filter = ('teacher',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'adress', 'teacher')
    search_fields = ('firstname', 'lastname', 'email', 'phone', 'adress', 'teacher__firstname', 'teacher__lastname')
    list_filter = ('teacher',)

