from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.name

class Course(models.Model):
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.title

class Candidate(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Candidature(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  school_name = models.CharField(max_length=100)
  status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
  applied_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.school_name} - {self.status}"