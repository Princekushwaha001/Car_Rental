from django.urls import path
from . import views 

urlpatterns = [
    path('', views.CarListView.as_view(), name='car-list'),
    path('car-detail/<slug:slug>/', views.CarDetailView.as_view(), name='car-details'),
]