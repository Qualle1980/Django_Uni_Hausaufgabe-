from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Studentenausweis(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="ausweis"
    )

    ausweisnummer = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.ausweisnummer


class Professor(models.Model):
    name = models.CharField(max_length=100)
    fachgebiet = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Semester(models.Model):
    bezeichnung = models.CharField(max_length=100)

    def __str__(self):
        return self.bezeichnung


class Kurs(models.Model):
    titel = models.CharField(max_length=100)

    professor = models.ForeignKey(
        Professor,
        on_delete=models.PROTECT,
        related_name="kurse"
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.PROTECT,
        related_name="kurse"
    )



    studenten = models.ManyToManyField(
        Student,
        related_name="kurse",
        blank=True
    )

    def __str__(self):
        return self.titel


class Kursbeschreibung(models.Model):
    kurs = models.OneToOneField(
        Kurs,
        on_delete=models.CASCADE,
        related_name="beschreibung"
    )

    text = models.TextField()

    def __str__(self):
        return f"Beschreibung: {self.kurs.titel}"