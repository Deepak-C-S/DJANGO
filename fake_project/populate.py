import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fake_project.settings')
django.setup()

from myapp.models import Employee
from faker import Faker


f=Faker('en_IN')

def populate(n):
    for i in range(n):
        name=f.name()
        dob=f.date_of_birth()
        job=f.job()
        place=f.city()
        email=f.email()

        s=Employee.objects.get_or_create(name=name, dob=dob, job=job, place=place, email=email)

populate(13)
