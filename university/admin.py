from django.contrib import admin
from .models import (
    Student,
    Studentenausweis,
    Professor,
    Semester,
    Kurs,
    Kursbeschreibung,
)

# Register your models here.
admin.site.register(Student)
admin.site.register(Studentenausweis)
admin.site.register(Professor)
admin.site.register(Semester)
admin.site.register(Kurs)
admin.site.register(Kursbeschreibung)

