from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','paid',
        'created', 'updated', 'orderType', 'orderStatus']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]