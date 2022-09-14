from dataclasses import fields
from pyexpat import model
from django import forms
from . import models


class StudentsRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Students
        fields="__all__"
        
        
class LearningFacilitatorsForm(forms.ModelForm):
    class Meta:
        model=models.LearningFacilitators
        fields="__all__"        