from django.db import models

# Create your models here.
class Student(models.Model):
    #name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    dept = models.TextField()
    sem = models.IntegerField()

