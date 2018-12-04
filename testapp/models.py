from django.db import models


# Create your models here.
class Customer(models.Model):


    Name = models.CharField(max_length=25)
    dob =models.DateField()
    age =models.IntegerField()
    email =models.EmailField(unique=True)
    mobno =models.CharField(max_length=25)

    class Meta:
        db_table='customer_details'


