from django.core.exceptions import ValidationError
from django.views.generic.detail import DetailView
from .models import Booking
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from razorpay.errors import SignatureVerificationError
from django.core.exceptions import ValidationError
from decimal import Decimal
from payments.models import Payment
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin



def payment_success(request):
    messages.success(request, "Booking Confirmed! Thank you for choosing us.")

    return redirect("my_bookings")

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_amount = self.object.total_amount
        if not total_amount or total_amount < Decimal("1.00"):
            raise ValidationError("Booking amount must be at least ₹1")
        amount_in_paise = int(self.object.total_amount * Decimal(100))
        client= razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
        )
        order = client.order.create({
            "amount": amount_in_paise,   # amount in paise
            "currency": "INR",
            "payment_capture": 1
        })
        context['order_id'] = order["id"]
        context['booking_id'] = self.object.id
        context['razorpay_key'] = settings.RAZORPAY_KEY_ID
        context['amount'] = float(total_amount)  # amount in rupees (for UI)
        return context


class BookingConfirmationView(DetailView):
    model = Booking
    template_name = 'bookings/booking_confirmation.html'
    context_object_name = 'booking'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payment = Payment.objects.get(booking=self.object)
        context['payment'] = payment
        return context


class MyBookingsView(TemplateView):
    model = Booking
    template_name = 'bookings/my_bookings.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.filter(user=self.request.user).order_by('-created_at')
        return context
    


class CancelBookingView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/cancel_booking.html'
    context_object_name = 'booking'

    def post(self, request, *args, **kwargs):
        booking = self.get_object()

        # Ensure user owns booking
        if booking.user != request.user:
            messages.error(request, "You cannot cancel this booking.")
            return redirect('my_bookings')

        if booking.booking_status in ['pending', 'confirmed']:
            booking.booking_status = 'cancelled'
            booking.save()
            messages.success(request, "Booking cancelled successfully.")
        else:
            messages.error(request, "This booking cannot be cancelled.")

        return redirect('my_bookings')