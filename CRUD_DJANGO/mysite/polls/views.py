from django.shortcuts import render
from .models import Student
from polls import forms

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('first_name')
    diction = {'title':"Index",'student-list': student_list}
    return render(request, 'myApp/index.html', context=diction)

def student_form(request):
    form = forms.StudentForm()

    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)

    diction = {'title' : "student_form", 'student_form': form}
    return render(request, 'myApp/student_form.html', context=diction)