from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Score, Subjects


class UserModel(UserAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "standard", "father_name", "roll_number")


class ScoreAdmin(admin.ModelAdmin):
    list_display = ("id", "semester", "subject_id", "subject_exam_marks", "subject_assignment_marks")


admin.site.register(Student, StudentAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Subjects)


admin.site.site_header = 'Administrator Page'



