from django.db import models


# Create your models here.
class Student(models.Model):
    Full_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=20)

    def __str__(self):
        return str(self.Full_name)
