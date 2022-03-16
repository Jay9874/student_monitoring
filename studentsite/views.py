from ast import Sub
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from matplotlib.style import context
from pandas import read_sql_query
from sklearn import model_selection
from .models import Subjects, Student, Score 
# from .models import Student, Score




def student_home(request):
    student = Student.objects.filter(admin=request.user.id)
    # student_obj = Student.objects.get(admin=request.user.id)
    # total_subjects = Subjects.objects.filter(student_id=student.id)

    subject_name = []

    context = {
        "student_list": student
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/home.html", context)


def scores(request):
    student = Student.objects.filter(admin=request.user.id)
    # score = Score.objects.filter(student_id=score.id)

    context = {
        "student_list": student,
        # "score_list": score
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/scores.html", context)



def analytics(request):
    student = Student.objects.filter(admin=request.user.id)
    # student_result = Score.objects.filter(student_id=student.id)
    context = {
        "student_list": student
    }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/analytics.html", context)
