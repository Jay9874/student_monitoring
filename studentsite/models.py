import email
from random import choices
from email.policy import default
from sre_constants import CATEGORY
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )


    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    gender = models.CharField(choices=GENDER, max_length=50, null=False, default="Male")
    father_name = models.CharField(max_length=64, null=True)
    mother_name = models.CharField(max_length=64, null=True,blank=True)
    standard = models.CharField(max_length=10, null=True)
    roll_number = models.BigIntegerField(default=0, null=True,)
    telephone = models.BigIntegerField(default=0, null=True)
    email = models.EmailField(blank=False, null=True, default="")
    residence = models.TextField(default=0, null=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='', default="")


    objects = models.Manager()
    def __str__(self):
        return self.first_name


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)


    objects = models.Manager()

    def __str__(self):
        return self.subject_name
class Score(models.Model):

    CATEGORY = (
    ('Semester 1', 'Semester 1'),
    ('Semester 2', 'Semester 2'),
    ('Semester 3', 'Semester 3'),
    ('Semester 4', 'Semester 4'),
    ('Semester 5', 'Semester 5'),
    ('Semester 6', 'Semester 6'),
    ('Semester 7', 'Semester 7'),
    ('Semester 8', 'Semester 8'),

    )
    id = models.AutoField(primary_key=True)
    # student_name = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, default=1)
    semester = models.CharField(max_length=64, choices=CATEGORY, null=True)
    subject_exam_marks = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)
    physics = models.CharField(max_length=64, default=0, null=True, blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.student_name