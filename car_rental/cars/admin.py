from django.contrib import admin
from .models import Car,Location,CarImage,CarType,Maintenance,Insurance
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'base_price_per_day', 'registration_number', 'status', 'current_location') 

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country')

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('car', 'provider', 'policy_number', 'start_date', 'end_date')

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('car','service_repair','maintenance_type', 'start_date', 'end_date', 'description')