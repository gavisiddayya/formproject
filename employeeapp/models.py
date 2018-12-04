from django.db import models

# Create your models here.
class Collage(models.Model):

    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        db_table= 'collage'


class Student(models.Model):

    name=models.CharField(max_length=4)
    rollno=models.IntegerField()
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=250)
    mobno=models.CharField(max_length=25)

    class Meta:
        db_table='student'