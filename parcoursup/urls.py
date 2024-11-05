from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses_list, name='courses_list'),
    path('apply/<int:course_id>/', views.apply, name='apply'),
    path('signup/', views.signup_view, name='signup'),  # Inscription
    path('login/', LoginView.as_view(template_name='parcoursup/login.html'), name='login'),  # Connexion
    path('logout/', LogoutView.as_view(), name='logout'),  # Déconnexion
    
]
