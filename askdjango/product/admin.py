from django.contrib import admin
from .models import Product, Product_bottom,Product_top



admin.site.register(Product_bottom)
admin.site.register(Product_top)

admin.site.register(Product)

# Register your models here.
