from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    studentID = models.IntegerField('学号', blank=True)
    phone = models.IntegerField('电话号码',blank = False)

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return self.username

class Company(AbstractUser):
    companyID = models.IntegerField('商号',blank=True)
    phone = models.IntegerField('电话号码',blank=False)

    class Meta:
        db_table = 'Company'

    def __str__(self):
        return self.username

class Cours(models.Model):
    lesson_name = models.CharField(max_length=50)
    summary = models.TextField()
    cmpany_associated = models.ManyToManyField(Company)
    student = models.ManyToManyField(Student)
    release_time = models.DateField()





