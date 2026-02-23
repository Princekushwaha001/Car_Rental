from django.db import models
from bookings.models import Booking
# Create your models here.

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True, choices=[
        ['credit_card', 'Credit Card'],
        ['debit_card', 'Debit Card'],
        ['paypal', 'PayPal'],
        ['bank_transfer', 'Bank Transfer']
    ])
    payment_status = models.CharField(max_length=50, null=True, blank=True, choices=[
        ['pending', 'Pending'],
        ['completed', 'Completed'],
        ['failed', 'Failed']
    ])
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} for Booking {self.booking.id}"