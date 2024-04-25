from django.db import models

# Create your models here.
class Patient(models.Model):
    pid=models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    condition=models.CharField(max_length=100)
    prescription=models.CharField(max_length=100)

    def __str__(self):
        return self.name
