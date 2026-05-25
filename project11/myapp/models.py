from django.db import models



# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    place = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()

    def str(self):
        return self.name