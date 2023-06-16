from django.contrib import admin
from .models import Cart, CartItem 
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('date_added', 'cart_id')
    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'is_active', 'quantity')
    

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)