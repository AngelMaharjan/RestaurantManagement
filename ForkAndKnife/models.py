from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

import datetime

# Create your models here.

class Customer(AbstractUser):
    phone_number = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.username

   #REQUIRED_FIELDS = ['email', 'number', 'address']




class Category(models.Model):
    category_id = models.AutoField;
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    subCategory_id = models.AutoField;
    name = models.CharField(max_length=20)
    category_id = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    menu_item_id = models.AutoField;
    name = models.CharField(max_length=100)
    desctription = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    item_image = models.ImageField(upload_to='media')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# 

class Order(models.Model):
    order_id = models.AutoField;
    #customer = models.ForeignKey(Custom, on_delete=models.CASCADE)
   # customer_contact = models.CharField(max_length=10)
    customer_address = models.CharField(max_length=100)
    order_items = models.ManyToManyField('Menu',through='OrderItem')
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateField(datetime.date, default="")
    bill = models.OneToOneField('Billing', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"Order #{self.id}"
    

class OrderItem(models.Model):
    OrderItem_id = models.AutoField;
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.item.name} ({self.item_price})"


# class Bill(models.Model):
    # bill_id = models.AutoField;
 #  bill_date = models.DateField(datetime)
    # total_price = models.DecimalField(max_digits=6, decimal_places=2)


class Billing(models.Model):
    billing_id = models.AutoField;
    orderr = models.ForeignKey(Order, on_delete=models.CASCADE, default="")
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    billed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billing for Order #{self.orderr.id}"









