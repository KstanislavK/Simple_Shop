from django.contrib import admin

from orderapp.models import OrderList, OrderItemList


class OrderItemInline(admin.TabularInline):
    model = OrderItemList
    raw_id_fields = ('product', )


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'email', 'phone_number', 'created_at')
    list_filter = ('created_at', )
    inlines = (OrderItemInline, )
