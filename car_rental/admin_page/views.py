from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from payments.models import Payment
from cars.models import Car, CarType, Location, Insurance, Maintenance
from bookings.models import Booking
from .forms import CarTypeForm, LocationForm, InsuranceForm, MaintenanceForm
from accounts.models import User


# ======================================================
# 🔥 CAR TYPE (ADD + EDIT + DELETE SAME PAGE)
# ======================================================

class CarTypeView(ListView):
    model = CarType
    template_name = "admin_page/car_type.html"
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.GET.get("edit")

        if pk:
            instance = get_object_or_404(CarType, pk=pk)
            context["form"] = CarTypeForm(instance=instance)
            context["edit_mode"] = True
            context["edit_id"] = pk
        else:
            context["form"] = CarTypeForm()
            context["edit_mode"] = False

        return context

    def post(self, request, *args, **kwargs):

        # DELETE
        if "delete_id" in request.POST:
            obj = get_object_or_404(CarType, pk=request.POST.get("delete_id"))
            obj.delete()
            messages.success(request, "Car Type deleted successfully.")
            return redirect("admin_car_type")

        # ADD / UPDATE
        pk = request.POST.get("edit_id")

        if pk:
            instance = get_object_or_404(CarType, pk=pk)
            form = CarTypeForm(request.POST, instance=instance)
            message = "Car Type updated successfully."
        else:
            form = CarTypeForm(request.POST)
            message = "Car Type added successfully."

        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("admin_car_type")

        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data(form=form))


# ======================================================
# 🔥 LOCATION (ADD + EDIT + DELETE SAME PAGE)
# ======================================================

class LocationView(ListView):
    model = Location
    template_name = "admin_page/location.html"
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.GET.get("edit")

        if pk:
            instance = get_object_or_404(Location, pk=pk)
            context["form"] = LocationForm(instance=instance)
            context["edit_mode"] = True
            context["edit_id"] = pk
        else:
            context["form"] = LocationForm()
            context["edit_mode"] = False

        return context

    def post(self, request, *args, **kwargs):

        if "delete_id" in request.POST:
            obj = get_object_or_404(Location, pk=request.POST.get("delete_id"))
            obj.delete()
            messages.success(request, "Location deleted successfully.")
            return redirect("admin_location")

        pk = request.POST.get("edit_id")

        if pk:
            instance = get_object_or_404(Location, pk=pk)
            form = LocationForm(request.POST, instance=instance)
            message = "Location updated successfully."
        else:
            form = LocationForm(request.POST)
            message = "Location added successfully."

        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("admin_location")

        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data(form=form))


# ======================================================
# 🔥 INSURANCE (ADD + EDIT + DELETE SAME PAGE)
# ======================================================

class InsuranceView(ListView):
    model = Insurance
    template_name = "admin_page/insurance.html"
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.GET.get("edit")

        if pk:
            instance = get_object_or_404(Insurance, pk=pk)
            context["form"] = InsuranceForm(instance=instance)
            context["edit_mode"] = True
            context["edit_id"] = pk
        else:
            context["form"] = InsuranceForm()
            context["edit_mode"] = False

        return context

    def post(self, request, *args, **kwargs):

        if "delete_id" in request.POST:
            obj = get_object_or_404(Insurance, pk=request.POST.get("delete_id"))
            obj.delete()
            messages.success(request, "Insurance deleted successfully.")
            return redirect("admin_insurance")

        pk = request.POST.get("edit_id")

        if pk:
            instance = get_object_or_404(Insurance, pk=pk)
            form = InsuranceForm(request.POST, instance=instance)
            message = "Insurance updated successfully."
        else:
            form = InsuranceForm(request.POST)
            message = "Insurance added successfully."

        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("admin_insurance")

        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data(form=form))


# ======================================================
# 🔥 MAINTENANCE (ADD + EDIT + DELETE SAME PAGE)
# ======================================================

class MaintenanceView(ListView):
    model = Maintenance
    template_name = "admin_page/maintenance.html"
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.GET.get("edit")

        if pk:
            instance = get_object_or_404(Maintenance, pk=pk)
            context["form"] = MaintenanceForm(instance=instance)
            context["edit_mode"] = True
            context["edit_id"] = pk
        else:
            context["form"] = MaintenanceForm()
            context["edit_mode"] = False

        return context

    def post(self, request, *args, **kwargs):

        if "delete_id" in request.POST:
            obj = get_object_or_404(Maintenance, pk=request.POST.get("delete_id"))
            obj.delete()
            messages.success(request, "Maintenance deleted successfully.")
            return redirect("admin_maintenance")

        pk = request.POST.get("edit_id")

        if pk:
            instance = get_object_or_404(Maintenance, pk=pk)
            form = MaintenanceForm(request.POST, instance=instance)
            message = "Maintenance updated successfully."
        else:
            form = MaintenanceForm(request.POST)
            message = "Maintenance added successfully."

        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("admin_maintenance")

        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data(form=form))


class BookingsView(ListView):
    model = Booking
    template_name = "admin_page/bookings.html"
    context_object_name = "objects"
    ordering = ['-created_at']

    def get_queryset(self):
        return Booking.objects.select_related(
            "user",
            "car",
            "pickup_location",
            "dropoff_location"
        ).all()

class PaymentsView(ListView):
    model = Payment
    template_name = "admin_page/payments.html"
    context_object_name = "objects"
    ordering = ['-paid_at']

    def get_queryset(self):
        return Payment.objects.select_related(
            "booking",
            "booking__user"
        ).all()


class UserView(ListView):
    model = User
    template_name = "admin_page/users.html"
    context_object_name = "objects"
    ordering = ['-id']

# ======================================================
# 🚗 CAR VIEWS (UNCHANGED)
# ======================================================

class AddCarView(CreateView):
    model = Car
    fields = [
        'car_type', 'current_location', 'brand', 'model', 'year',
        'registration_number', 'status', 'color',
        'mileage', 'seats', 'fuel_type', 'transmission',
        'image', 'base_price_per_day',
    ]
    template_name = 'admin_page/add_car.html'
    success_url = reverse_lazy('admin_car_list')


class UpdateCarView(UpdateView):
    model = Car
    fields = [
        'car_type', 'current_location', 'brand', 'model', 'year',
        'registration_number', 'status', 'color',
        'mileage', 'seats', 'fuel_type', 'transmission',
        'image', 'base_price_per_day',
    ]
    template_name = 'admin_page/update_car.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('admin_car_list')


class ListCarView(ListView):
    model = Car
    template_name = 'admin_page/list_car.html'
    context_object_name = 'cars'
    ordering = ['-id']


class DetailCarView(DetailView):
    model = Car
    template_name = 'admin_page/detail_car.html'
    context_object_name = 'car'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.filter(
            car=self.object
        ).order_by('-created_at')
        return context


class DeleteCarView(DeleteView):
    model = Car
    template_name = 'admin_page/delete_car.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('admin_car_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Car deleted successfully.")
        return super().delete(request, *args, **kwargs)