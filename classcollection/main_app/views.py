from django.shortcuts import render
from django.http.response import HttpResponsePermanentRedirect
from django.http import HttpResponse
# Create your views here.

class Classroom:
    def __init__(self, name, favclass, role, age):
        self.name = name
        self.favclass = favclass
        self.role = role
        self.age = age

classrooms = [
    Classroom('Caroline', 'science', 'student', 13),
    Classroom('Maria', 'science', 'teacher', 28),
    Classroom('Adalia', 'english', 'student', 11),
    Classroom('Christine', 'science', 'teacher', 28),
    Classroom('Waverly', 'science', 'student', 11),
    Classroom('Lucy', 'Latin', 'student', 11),
    Classroom('Mia', 'science', 'student', 12),
    Classroom('Soraya', 'history', 'student', 12),
    Classroom('Aldea', 'math', 'student', 11),
] 

def home(request):
    return HttpResponse('<h1>Hello class</h1>')

def about(request):
    return render(request, 'about.html')

def class_index(request):
    return render(request, 'class/index.html', { 'classrooms' : classrooms })