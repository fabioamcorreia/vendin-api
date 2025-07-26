from django.contrib import admin
from .models import Client, Product, Order, OrderItem, Contact

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'nif', 'email')
    search_fields = ('name', 'nif', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'created_at')
    inlines = [OrderItemInline]
    list_filter = ('created_at',)
    search_fields = ('client__name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'client')
    search_fields = ('user__username', 'client__name')
