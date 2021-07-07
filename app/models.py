from django.db import models

# Create your models here.
class School(models.Model):
    student_name=models.CharField(max_length=30)
    subject_name=models.CharField(max_length=30)
    marks=models.IntegerField()

    def __str__(self):
        return self.student_name 