from django import forms 
from cars.models import Car,Location
from datetime import timedelta
from django.utils import timezone

class BookCar(forms.Form):
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),label="Start Date")
    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),label="End Date")
    
    pickup_location = forms.ModelChoiceField(queryset=
                                             Location.objects.none(), label="Pickup Location")
    dropoff_location = forms.ModelChoiceField(queryset=Location.objects.all(), label="Dropoff Location")

    def __init__(self, *args, **kwargs):
        car_name = kwargs.pop('car_name', None)
        super().__init__(*args, **kwargs)
        if car_name:
            current_location_id = [car.current_location.id for car in 
                                Car.objects.filter(model=car_name)]
            self.fields['pickup_location'].queryset = Location.objects.filter(id__in=current_location_id)
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if not start_date or not end_date:
            return cleaned_data 
        now = timezone.now()
        if start_date >= end_date:
            raise forms.ValidationError("End date must be after start date.")
        if start_date < now + timedelta(hours=3):
            raise forms.ValidationError("Start date must be at least 3 hours from now.")
        return cleaned_data

