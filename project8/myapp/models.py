from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
    usn=models.CharField(max_length=20)
    dept=models.CharField(max_length=50)
    college=models.CharField(max_length=100)

    def __str__(self):
        return self.name


