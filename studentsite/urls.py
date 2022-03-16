from django.urls import path
from . import views

app_name = "studentsite"

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("analytics", views.analytics, name="analytics"),
    path("scores", views.scores, name="scores")
] 