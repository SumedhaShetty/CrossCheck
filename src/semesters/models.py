from django.db import models
from django.urls import reverse
# Create your models here.


class Department(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Semester(models.Model):
    title = models.CharField(max_length=100)
    dept_link = models.ManyToManyField(Department)

   # d = Department.objects.filter(COMPUTERS)

    def __str__(self):
        return self.title
    
class Subjects(models.Model):
    title = models.CharField(max_length=100)
    sem_link = models.ManyToManyField(Semester)

    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    sub_link = models.ForeignKey(Subjects, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Data(models.Model):
    title = models.CharField(max_length=100)
    page_no = models.IntegerField()
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    book_link = models.ForeignKey(Book, on_delete= models.CASCADE)
   
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("semesters:post_detail",kwargs={"id": self.id})
       # return "/semesters/sems/%s/" %(self.id)