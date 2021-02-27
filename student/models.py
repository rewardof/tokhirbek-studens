from django.db import models
from django import forms


class Student(models.Model):
    full_name = models.CharField(max_length=30)
    entry_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, max_length=254)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, max_length=1, default='math')
    interests = models.TextField(max_length=200, blank=True)
    password = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Marks(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    mark_for_subject = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.student}--{self.course}--mark:{self.mark_for_subject}'

    class Meta:
        verbose_name_plural = "Marks"

class Course(models.Model):
    # choices = (
    #     ('M', 'math'),
    #     ('P', 'physics'),
    #     ('MC', 'mechanics'),
    #     ('H', 'history'),
    #     ('B', 'biology'),
    #     ('E', 'english'),
    #     ('C', 'chemicals'),
    #     ('R', 'right'),
    #     ('E', 'economy'),
    # )
    # STR_CHOICES = {key: value for (key, value) in choices}
    name = models.CharField(max_length=20, unique=True)
    faculties = models.ManyToManyField("Faculty", related_name="faculty")

    def __str__(self):
        return self.name


class Faculty(models.Model):
    # choices = [
    #     ('T', 'technology'),
    #     ('M', 'medicine'),
    #     ('F', 'finance'),
    #     ('P', 'politics'),
    #     ('S', 'social subjects'),
    # ]
    # STR_CHOICES = {key: value for (key, value) in choices}
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Faculties"


class Teacher(models.Model):
    full_name = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name}--{self.course}'

