from django.contrib import admin

from .models import Customer, Menu, Category, SubCategory, OrderItem, Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(OrderItem)



