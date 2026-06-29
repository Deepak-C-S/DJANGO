from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    sem1 = models.PositiveIntegerField(blank=True, null=True)
    sem2 = models.PositiveIntegerField(blank=True, null=True)
    sem3 = models.PositiveIntegerField(blank=True, null=True)
    sem4 = models.PositiveIntegerField(blank=True, null=True)
    sem5 = models.PositiveIntegerField(blank=True, null=True)
    sem6 = models.PositiveIntegerField(blank=True, null=True)
    sem7 = models.PositiveIntegerField(blank=True, null=True)
    sem8 = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return f"{self.name} ({self.subject})"
    
# StudentSemesterSummary removed — semester fields moved onto Student for simplicity
