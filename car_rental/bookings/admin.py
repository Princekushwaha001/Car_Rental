from django.contrib import admin
from .models import Booking
# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'booking_status', 'total_amount')