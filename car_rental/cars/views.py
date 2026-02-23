from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Car,CarImage,Location
from bookings.forms import BookCar
from bookings.models import Booking
from django.http import HttpResponse 
# Create your views here.

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookcar_form'] = BookCar(car_name=self.object.model)
        return context
    
    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print(request.POST,"post data in car detail view")
        form = BookCar(request.POST,car_name=self.object.model)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            dropoff_location = form.cleaned_data['dropoff_location']
            pickup_location = form.cleaned_data['pickup_location']
            booking = Booking.objects.create(
                car=self.object,user=request.user,start_date=start_date,end_date=end_date,booking_status='pending',
                price_per_day=self.object.base_price_per_day,
                total_days=(end_date - start_date).days,
                total_amount=self.object.base_price_per_day * (end_date - start_date).days,
                pickup_location=pickup_location,
                dropoff_location=dropoff_location)
            return redirect(f'/bookings/booking-summary/{booking.slug}/')  
        else:
            context['bookcar_form'] = form
        return self.render_to_response(context)
    