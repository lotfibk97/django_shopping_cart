from django.contrib import admin

from .models import Cart, Product, Order

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
