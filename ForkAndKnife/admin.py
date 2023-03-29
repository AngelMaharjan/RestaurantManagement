from django.contrib import admin

from .models import Menu, Category, SubCategory
# Register your models here.

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(SubCategory)