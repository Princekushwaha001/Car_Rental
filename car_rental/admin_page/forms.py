from django import forms
from cars.models import CarType, Location, Insurance, Maintenance


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Name'
        })
        
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Description',
            'rows': 4
        })


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['name'].widget.attrs.update({'placeholder': 'Name'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City'})
        self.fields['state'].widget.attrs.update({'placeholder': 'State'})
        self.fields['country'].widget.attrs.update({'placeholder': 'Country'})
        self.fields['pincode'].widget.attrs.update({'placeholder': 'Pincode'})
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Address',
            'rows': 3
        })


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = "__all__"
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['provider'].widget.attrs.update({'placeholder': 'Provider'})
        self.fields['policy_number'].widget.attrs.update({'placeholder': 'Policy Number'})
        self.fields['coverage_details'].widget.attrs.update({
            'placeholder': 'Coverage Details',
            'rows': 4
        })



class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = "__all__"
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['maintenance_type'].widget.attrs.update({'placeholder': 'Maintenance Type'})
        self.fields['service_repair'].widget.attrs.update({'placeholder': 'Service / Repair'})
        self.fields['cost'].widget.attrs.update({'placeholder': 'Cost'})
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Description',
            'rows': 4
        })