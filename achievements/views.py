from django.shortcuts import render
from ast import Sub
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from matplotlib.style import context
from pandas import read_sql_query
from sklearn import model_selection
from studentsite.models import Student, Score, Cocurriculum, Achievement, Remark

# Create your views here.
def academics(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "achievements/academics.html", context)


def co_curriculum(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "achievements/co_curriculum.html", context)



def others(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "achievements/others.html", context)