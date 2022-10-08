from django.contrib import admin

from apartment.models import Apartment, Floor


# Register your models here.

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "room_quantity", "area", "floor", "price", "image_3d", "image_2d", "image"]


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ["id", "floor_id", "name"]
