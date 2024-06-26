from django.contrib import admin
from .models import Person, Vehicle, Officer


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("license_plate", "brand", "color", "person")
    search_fields = ("license_plate", "brand", "color")
    list_filter = ("brand", "color")


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ("name", "unique_id")
    search_fields = ("name", "unique_id")
