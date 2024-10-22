from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_list, name='courses_list'),
    path('apply/<int:course_id>/', views.apply, name='apply'),
]
