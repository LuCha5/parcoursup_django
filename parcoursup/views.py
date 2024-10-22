from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Course

def index(request):
    return HttpResponse("Bonjour")


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'parcoursup/courses_list.html', {'courses': courses})


def apply(request, course_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = Course.objects.get(id=course_id)
        Candidate.objects.create(name=name, email=email, course=course)
        return redirect('courses_list')
    return render(request, 'parcoursup/apply.html', {'course_id': course_id})
