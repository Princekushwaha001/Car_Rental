from django.db import models
from accounts.models import User
from cars.models import Car,Location

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    total_days = models.IntegerField(null=True, blank=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    booking_status = models.CharField(max_length=50, null=True, blank=True, choices=[
        ['pending', 'Pending'],
        ['confirmed', 'Confirmed'],
        ['cancelled', 'Cancelled'],
        ['completed', 'Completed']
    ])
    pickup_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='pickup_location')
    dropoff_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, 
                                         related_name='dropoff_location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs) 
        if is_new and not self.slug:
            self.slug = (
                f"booking-{self.pk}-"
                f"{self.start_date.strftime('%Y%m%d')}-"
                f"{self.end_date.strftime('%Y%m%d')}-"
                f"{self.user.username}"
            ).lower().replace(" ", "-")

            super().save(update_fields=['slug'])
    def __str__(self):
        return f"Booking {self.id} by {self.user.username} for {self.car.model}"