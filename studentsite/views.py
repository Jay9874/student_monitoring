from ast import Sub
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from matplotlib.style import context
from pandas import read_sql_query
from sklearn import model_selection
from .models import Subject, Student, Score, Cocurriculum, Achievement, Remark




def student_home(request):
    student = Student.objects.filter(student=request.user.id)
    # student_obj = Student.objects.get(admin=request.user.id)
    # total_subjects = Subjects.objects.filter(student_id=student.id)

    # subject_name = []

    context = {
        "student_list": student
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/home.html", context)


def scores(request):
    student = Student.objects.get(student=request.user.id)
    score = Score.objects.filter(student=student)

    context = {
        "student_list": student,
        "scores": score
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/scores.html", context)



def analytics(request):
    student = Student.objects.filter(student=request.user.id)
    # # student_result = Score.objects.filter(student_id=student.id)

    context = {
        "student_list": student
    }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/analytics.html", context)


def cocurriculum(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/cocurriculum.html", context)


def achievement(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/achievement.html", context)

def remark(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/remark.html", context)