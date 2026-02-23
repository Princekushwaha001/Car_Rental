from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True,choices=[
        ['customer', 'Customer'],
        ['staff', 'Staff']
    ])
    driving_license_no = models.CharField(max_length=100, null=True, blank=True)
    license_expiry_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)