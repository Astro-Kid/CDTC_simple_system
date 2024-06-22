from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)

    def __str__(self):
        return self.name
