from django.db import models
from django import forms


class Student(models.Model):
    choices =  [
    ('T', 'technology'),
    ('M', 'medicine'),
    ('F', 'Finance'),
    ('P', 'politics'),
    ('s', 'social subjects'),
]
    ful_name = models.CharField(max_length=30)
    student_id = models.IntegerField(max_length=6)
    entry_date = models.DateTimeField(auto_now_add=True, widjet=forms.SelectDateWidjet)
    email = models.EmailField(blank=True, max_length=254)
    faculty = models.CharField(choices=choices, max_length=1)
    interests = models.TextField(max_length=200, blank=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name}--{self.last_name}'


class Marks(models.Model):
    subject = models.CharField(max_length=30)
    mark_for_subject = models.DecimalField(max_digits=4, decimal_places=2)


class Faculty(models.Model):
    subject = models.CharField(max_length=2)


class Teacher(models.Model):
    full_name = models.CharField(max_length=20)
    teacher_id = models.IntegerField(max_length=6)
    t_subject = models.CharField(max_length=30)

