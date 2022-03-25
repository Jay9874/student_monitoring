from cProfile import label
import email
from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
from turtle import ondrag
from django.conf import settings
from random import choices
from email.policy import default
from sre_constants import CATEGORY
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from django.contrib.auth.models import User, UserManager
from pytz import timezone


class Student(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    student = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64, null=True, blank=False)
    last_name = models.CharField(max_length=64, null=True)
    gender = models.CharField(choices=GENDER, max_length=50, null=False, default="Male")
    father_name = models.CharField(max_length=64, null=True)
    mother_name = models.CharField(max_length=64, null=True)
    standard = models.CharField(max_length=10, null=True)
    roll_number = models.BigIntegerField(default=0, null=True,)
    telephone = models.BigIntegerField(default=0, null=True)
    email = models.EmailField(blank=False, null=True, default="")
    residence = models.TextField(default=0, null=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='', default="", blank=False)
    birthday = models.DateField( blank=False, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.first_name


# class Semester(models.Model):
    
#     SEMESTER = (
#         ('Semester 1', 'Semester 1'),
#         ('Semester 2', 'Semester 2'),
#         ('Semester 3', 'Semester 3'),
#         ('Semester 4', 'Semester 4'),
#         ('Semester 5', 'Semester 5'),
#         ('Semester 6', 'Semester 6'),
#         ('Semester 7', 'Semester 7'),
#         ('Semester 8', 'Semester 8')
#     )


#     student = models.ManyToManyField(Student, blank=False)
#     semester = models.CharField(max_length=64, blank=False, choices=SEMESTER )
    

#     def __str__(self):
#         return self.semester

        
# class Subject(models.Model):

#     student = models.ManyToManyField(Student, blank=False)
#     semester = models.ManyToManyField(Semester, blank=False)
#     subject_name = models.CharField(max_length=255)
#     subject_exam_marks = models.FloatField(max_length=64, null=True, blank=True)
#     subject_assingment_marks = models.FloatField(max_length=64, null=True, blank=True)

#     objects = models.Manager()

#     def __str__(self):
#         return self.subject_name


class Score(models.Model):

    # id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject, blank=False, on_delete=models.CASCADE, null=True)
    # semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE, blank=False)
    # subject_exam_marks = models.FloatField(default=0)
    # subject_assignment_marks = models.FloatField(default=0)
    physics_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    physics_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    mathematics_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    mathematics_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    chemistry_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    chemistry_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    biology_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    biology_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    computer_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    computer_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    hindi_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    hindi_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    english_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    english_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    history_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    history_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    geography_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    geography_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    sanskrit_exam_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)
    sanskrit_assingment_marks = models.FloatField(max_length=64, default=0, null=True, blank=False)



    objects = models.Manager()


class Cocurriculum(models.Model):

    SPORTS = (
        ('Cricket', 'Cricket'),
        ('Football', 'Football'),
        ('Race', 'Race'),
        ('Kabaddi', 'Kabaddi'),
        ('Tennis', 'Tennis')
    )

    Grade = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D+', 'D+'),
        ('D', 'D')
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE, blank=False)
    sports = models.CharField( max_length=64, choices=SPORTS, blank=True)
    singing = models.CharField(max_length=10, choices=Grade, default="", blank=True)
    dancing = models.CharField(max_length=10, choices=Grade, default="", blank=True)
    drawing = models.CharField(max_length=10, choices=Grade, default="", blank=True)
    essays = models.CharField(max_length=10, choices=Grade, default="", blank=True)
    presents = models.CharField(max_length=10, choices=Grade, default="", blank=True)

    objects = models.Manager()


class Achievement(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE, blank=False)
    academic_achievements = models.ImageField(upload_to='', default="", blank=False)
    additional_achievements = models.ImageField(upload_to='', default="", blank=False)

    objects = models.Manager()
class Remark(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE, blank=False)
    teacher_thought = models.CharField(max_length=800, default="", blank=False, null=True)

    objects = models.Manager()
