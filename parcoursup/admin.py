from django.contrib import admin
from .models import School, Course, Candidate, Candidature

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Candidate)
admin.site.register(Candidature)
