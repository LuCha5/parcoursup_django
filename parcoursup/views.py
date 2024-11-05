from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Candidate, Course

def index(request):
    return HttpResponse("Bonjour")

@login_required
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'parcoursup/courses_list.html', {'courses': courses})

@login_required
def apply(request, course_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = Course.objects.get(id=course_id)
        Candidate.objects.create(name=name, email=email, course=course)
        return redirect('courses_list')
    return render(request, 'parcoursup/apply.html', {'course_id': course_id})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('courses_list')  # Redirige vers la page des cours
    else:
        form = UserCreationForm()
    return render(request, 'parcoursup/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('courses_list')
    else:
        form = AuthenticationForm()
    return render(request, 'parcoursup/login.html', {'form': form})
