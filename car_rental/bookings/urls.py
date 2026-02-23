from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('booking-summary/<slug:slug>/',views.BookingDetailView.as_view(),name ='booking'),
    path('booking-confirmation/<slug:slug>/',views.BookingConfirmationView.as_view(),name ='booking-confirmation'), 
    path('my-bookings/',login_required(views.MyBookingsView.as_view()), name = 'my_bookings'),
    path('cancel-booking/<int:pk>/',views.CancelBookingView.as_view(), name='cancel_booking')
    
]