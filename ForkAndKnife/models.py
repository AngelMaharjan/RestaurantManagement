from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

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
# class Order(models.Model):
    # order_id = models.AutoField;
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # food_items = 
# 








