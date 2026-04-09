from django.contrib import admin
from .models import Order
from .models import Vendor
admin.site.register(Vendor)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "city", "total_amount", "status", "payment_method", "date_ordered")
    list_filter = ("status", "payment_method")
    search_fields = ("full_name", "email", "phone")
    fields = ("full_name", "email", "phone", "address", "city", "total_amount", "status", "payment_method")

admin.site.register(Order, OrderAdmin)