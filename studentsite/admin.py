from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Score, Cocurriculum, Achievement, Remark


class UserModel(UserAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "standard", "father_name", "roll_number")


class ScoreAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "physics_exam_marks", "physics_assingment_marks")


class CocurriculumAdmin(admin.ModelAdmin):
    list_display = ("student", "sports", "drawing", "singing", "dancing", "essays", "presents")

class AchievementAdmin(admin.ModelAdmin):
    list_display = ("academic_achievements", "additional_achievements")

class RemarkAdmin(admin.ModelAdmin):
    list_display = ("student", "teacher", "teacher_thought",)




# class SemesterAdmin(admin.ModelAdmin):
#     list_display = ("semester",)
#     filter_horizontal = ("student",)



# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ("subject_name",)
#     filter_horizontal = ("semester",)




# admin.site.register(Semester, SemesterAdmin)
admin.site.register(Remark, RemarkAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Cocurriculum, CocurriculumAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Score, ScoreAdmin)
# admin.site.register(Subject, SubjectAdmin)


admin.site.site_header = 'Administrator Page'



