from django.db import models

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
