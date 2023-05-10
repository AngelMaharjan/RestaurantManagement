from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from django.utils import timezone
# Create your models here.



class Customer(AbstractUser):
    phone_number = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Customer"





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
# class Cart(models.Model):
    # user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Menu, through='OrderItem')
    # created_at = models.DateTimeField(auto_now= True,)
# 
    # def __str__(self):
        # return f'{self.user.username} - {self.total_cost}'
# 
    # @property
    # def total_cost(self):
        # return sum(item.total_price for item in self.order_items.all())
# 

'''
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default= None)
    #cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
    customer_address = models.CharField(max_length=100)
   # order_items = models.ManyToManyField('Menu',through='OrderItem')
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=30, default="Cash on Delivery")
    order_date = models.DateField(auto_now_add=True)
    
   # bill = models.OneToOneField('Billing', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"Order #{self.id}  - {self.total_price}"
        
        '''
    
'''
class OrderItem(models.Model):
   # cart = models.ForeignKey(Cart, on_delete=models.CASCADE,default=None ,related_name= 'order_items')
   # order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Menu, on_delete=models.CASCADE, default= None)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.item.name} ({self.item_price})"
    
    @property
    def total_price(self):
        return self.price * self.quantity '''


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    payment_method = models.CharField(max_length=30, default="Cash on Delivery")
    delivery_address = models.CharField(max_length=100, default="")

    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Order"

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum(item.get_total for item in order_items)
        return total



class OrderItem(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
   # order = models.ForeignKey(Order, on_delete=models.CASCADE, null= True, default="")

    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
  #  order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    @property
    def get_total(self):
        total = round (self.item.price * self.quantity)
        return total

'''
class Billing(models.Model):
    billing_id = models.AutoField;
   # orderr = models.ForeignKey(Order, on_delete=models.CASCADE, default="")
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    billed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billing for Order #{self.orderr.id}"
    '''









# 
# class Cart(models.Model):
    # user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # quantity = models.PositiveIntegerField(default=1)
    # special_instructions = models.TextField(blank=True)
# 
    # def __str__(self):
        # return f"{self.quantity} x {self.item} for {self.user}"
# 