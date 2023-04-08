from django.contrib import admin

from apps.order.models import Order


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "user", "apartment", "status"]
