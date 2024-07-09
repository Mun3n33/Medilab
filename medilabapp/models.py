from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Admission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    medicalhistory = models.TextField()
    phone = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=10)
    staff = models.IntegerField()

    def __str__(self):
        return self.name
