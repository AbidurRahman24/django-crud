from django import forms
from my_app import models

class StudentForm(forms.Form):
    class Meta:
        model = models
        fields = '__all__'