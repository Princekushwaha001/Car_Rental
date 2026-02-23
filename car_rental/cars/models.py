from django.db import models

# Create your models here.

class CarType(models.Model):
    type_name = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.type_name
    
class Location(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    pincode = models.CharField(max_length=20,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.city}, {self.state}"
    
class Car(models.Model):
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True, blank=True)
    current_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.CharField(max_length=100,null=True, blank=True)
    model = models.CharField(max_length=100,null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    registration_number = models.CharField(max_length=100,null=True, blank=True)
    status = models.BooleanField(default=True) 
    color = models.CharField(max_length=50,null=True, blank=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    fuel_type = models.CharField(max_length=50,null=True, blank=True)
    transmission = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to='car_images/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    base_price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.brand}-{self.model}-{self.registration_number}".lower().replace(" ", "-")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f" {self.model} ({self.registration_number})"
    
    
class Insurance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    provider = models.CharField(max_length=100,null=True, blank=True)
    policy_number = models.CharField(max_length=100,null=True, blank=True)
    coverage_details = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Insurance for {self.car} by {self.provider}"
    
class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=100,null=True, blank=True)
    service_repair = models.CharField(max_length=100,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Maintenance for {self.car} on {self.start_date}"
    
class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='car_images/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.car} uploaded on {self.uploaded_at}"