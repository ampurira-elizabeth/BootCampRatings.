# from ast import If
from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
def register_students(request):
    if request.method=="POST":
        form=forms.StudentsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= forms.StudentsRegistrationForm()
    return render(request,"rating/register_student.html",{"form":form})

def list_students(request):
    students=models.Students.objects.all()
    return render(request, "rating/students_list.html",{"students":students})

def register_learningfacilitators(request):
    if request.method=="POST":
        form= forms.LearningFacilitatorsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= forms.LearningFacilitatorsForm()  
    return render(request,"rating/register_facilitator.html",{"form":form})   

def list_facilitators(request):
    facilitators= models.LearningFacilitators.objects.all()
    return render(request,"rating/facilitators_list.html",{"facilitators":facilitators})       