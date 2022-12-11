from django.db import models

class Contact(models.Model):
    Email=models.CharField(max_length=40)
    Name=models.CharField(max_length=40)
    Textarea=models.CharField(max_length=2000)
    def __str__(self):
        return self.Name


class Order(models.Model):
     Name=models.CharField(max_length=40)
     Mobileno=models.IntegerField(max_length=10)
     Address=models.CharField(max_length=200)
     Icecream=models.CharField(max_length=60)
     def __str__(self):
        return self.Name
class Account(models.Model):
    Username=models.CharField(max_length=40)
    Email=models.CharField(max_length=40)
    Contact=models.CharField(max_length=40)
    Password=models.CharField(max_length=40)
    def __str__(self):
        return self.Username



   

