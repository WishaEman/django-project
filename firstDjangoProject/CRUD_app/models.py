from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=11)

    def __str__(self):
        return self.emp_name