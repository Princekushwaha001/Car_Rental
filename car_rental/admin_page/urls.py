from django.urls import path
from . import views
from .decorators import staff_required

urlpatterns = [


    path("car-types/", staff_required(views.CarTypeView.as_view()), name="admin_car_type"),
    path("locations/", staff_required(views.LocationView.as_view()), name="admin_location"),
    path("insurances/", staff_required(views.InsuranceView.as_view()), name="admin_insurance"),
    path("maintenances/", staff_required(views.MaintenanceView.as_view()), name="admin_maintenance"),
    path("bookings/", staff_required(views.BookingsView.as_view()), name="admin_bookings"),
    path("payments/", staff_required(views.PaymentsView.as_view()), name="admin_payments"),
    path("users/", staff_required(views.UserView.as_view()), name="admin_users"),


    path("add_car/", staff_required(views.AddCarView.as_view()), name="admin_add_car"),
    path("update_car/<slug:slug>/", staff_required(views.UpdateCarView.as_view()), name="admin_update_car"),
    path("list_car/", staff_required(views.ListCarView.as_view()), name="admin_car_list"),
    path("detail_car/<slug:slug>/", staff_required(views.DetailCarView.as_view()), name="admin_detail_car"),
    path("delete_car/<slug:slug>/", staff_required(views.DeleteCarView.as_view()), name="admin_delete_car"),
]