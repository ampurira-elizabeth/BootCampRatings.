

from django.db import models
from django.utils import timezone

# Create your models here.
class Students(models.Model):
    student_name= models.CharField(max_length=15,null=True)
    student_id= models.SmallIntegerField(null=True)
    student_course= models.CharField( max_length=20, null=True)
    student_choices=(
        ('Very Unsatisfied','-2'),
        ('Unsatisfied','-1'),
        ('Nuetral','0'),
        ('Satisfied','1'),
        ('Very Satisfied','2')
    )
    student_scores= models.CharField(max_length=30,choices=student_choices,null=True)
    gender_choices=(
        ('M','male'),
        ('F','female'),
        ('O', 'other')
    )
    gender=models.CharField(max_length=6,choices=gender_choices, null=True)
    date=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.student_scores    

    
class LearningFacilitators(models.Model):
    lf_name= models.CharField(max_length=15,null=True)
    students_choices=(
        ('very unsatisfied','-2'),
        ('unsatisfied','-1'),
        ('nuetral','0'),
        ('satisfied','1'),
        ('very satisfied','2')
    )
    students_scores= models.CharField(max_length=20,choices=students_choices,null=True)
    student_name= models.CharField(max_length=15,null=True)
    date=models.DateTimeField(default=timezone.now)


  
        