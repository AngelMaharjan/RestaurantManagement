from django.contrib import admin

from .models import Menu, Category, SubCategory, Customer, Order
# Register your models here.

admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Order)