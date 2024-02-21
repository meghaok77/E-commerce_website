from django.db import models

class userdetails(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=50,null=True)

class category(models.Model):
    category_name=models.CharField(max_length=50)
    category_image=models.ImageField(upload_to="categories",default="null.jpg")

class product(models.Model):
    product_category = models.ForeignKey(category, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to="products",default="null.jpg")
    product_description=models.TextField(max_length=100)
    product_price=models.IntegerField()




    




# Create your models here.
