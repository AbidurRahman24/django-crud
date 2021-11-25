from django.shortcuts import render
from my_app import forms

# Create your views here.
def index(request):
    diction = {'title' : "index"}
    return render(request, 'my_app/index.html', context=diction)

def student_form(request):
    form = forms.StudentForm()
    diction = {'title' : "student_form", 'student_form': form}
    return render(request, 'my_app/student_form.html', context=diction)