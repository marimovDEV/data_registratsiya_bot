from django.shortcuts import render
from .models import Lessons,Now_Lessons,New_Lessons,Students


# Create your views here.

def index(request):
    return render(request,'index.html',{'title':'home page'})

def lessons(request):
    lessons = Lessons.objects.all()
    new_lessons = New_Lessons.objects.all()
    now_lessons = Now_Lessons.objects.all()
    return render(request,'lessons.html',{'title':'lessons page','lessons':lessons,'new_lessons':new_lessons,'now_lessons':now_lessons})

def students(request):
    students = Students.objects.all()
    return render(request,'students.html',{'title':'students page','students':students})

