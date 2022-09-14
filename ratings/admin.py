from django.contrib import admin
from .models import Students
from .models import LearningFacilitators
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display=('student_name','student_id','student_scores')
    search_fields=('student_name','student_scores')
admin.site.register(Students,StudentsAdmin) 

class LearningFAdmin(admin.ModelAdmin):
    list_display=('lf_name','students_scores')
    search_fields=('lf_name','students_scores')
admin.site.register(LearningFacilitators,LearningFAdmin)    