from django.shortcuts import render
import json
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from razorpay.errors import SignatureVerificationError
from .models import Payment
from bookings.models import Booking 
from django.utils import timezone

# Create your views here.
def create_order(request):
    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )

    order = client.order.create({
        "amount": 50000,  # ₹500 in paise
        "currency": "INR",
        "payment_capture": 1
    })
    context = {
        "order_id": order["id"],
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "amount": 500
    }
    return render(request, "payment.html", context)



@csrf_exempt
def verify_payment(request,booking_id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)
    try:
        data = json.loads(request.body)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        params_dict = {
            "razorpay_order_id": data.get("razorpay_order_id"),
            "razorpay_payment_id": data.get("razorpay_payment_id"),
            "razorpay_signature": data.get("razorpay_signature"),}
        client.utility.verify_payment_signature(params_dict)
        booking = Booking.objects.get(id=booking_id)
        payment_data = client.payment.fetch(data["razorpay_payment_id"])
        payment_method = payment_data["method"]
        Payment.objects.create(
            booking=booking,
            amount=booking.total_amount,
            payment_method=payment_method,
            payment_status="completed",
            transaction_id=data["razorpay_payment_id"],
            paid_at=timezone.now()
        )
        booking.booking_status = "confirmed"
        booking.save()

        return JsonResponse({"status": "success","message": "Payment verified"})

    except SignatureVerificationError:
        return JsonResponse({"status": "failed","message": "Signature verification failed"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error","message": str(e)}, status=500)

def payment_success(request):

    return render(request, "payment_success.html")

def payment_failed(request):
    return render(request, "payment_failed.html")

