from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student')