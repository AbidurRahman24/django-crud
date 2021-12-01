from django import forms
from polls import models

class StudentForm(forms.ModelForm):
    class meta:
        model = models.Student
        fields = "__all__"