from django.contrib import admin
from LittleLemonAPI.models import Order, MenuItem, Category, OrderItem, Cart

admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Category)