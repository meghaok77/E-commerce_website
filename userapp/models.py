from django.db import models
from adminapp.models import *

class Adminlogin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)


class Cart(models.Model):
    uid=models.ForeignKey(userdetails, on_delete=models.CASCADE)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()

class Review(models.Model):
    uid=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    review=models.CharField(max_length=250)
    rating=models.FloatField(null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

class Contact(models.Model):
    uid=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=250)
class Carttotal1(models.Model):
    uid=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    subtotal=models.IntegerField()
    total=models.IntegerField()


class Paymentdetails(models.Model):
    uid=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address1=models.TextField(max_length=100)
    address2=models.TextField(max_length=100)
    email=models.EmailField()
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()
    payment_mode=models.CharField(max_length=50)

    

    


    


# Create your models here.
