from django.db import models
from django.db.models.functions import Now
from phonenumber_field.modelfields import PhoneNumberField

from appointment.utils.view_helpers import generate_random_id
from appointment.utils.date_time import get_timestamp

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(db_default=Now())
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Vehicle(models.Model):
    vin = models.CharField(max_length=40)
    part = models.CharField(max_length=200, default="TBD")
    labor = models.CharField(max_length=200, default="TBD")

    make = models.CharField(max_length=200, default="TBD")
    model = models.CharField(max_length=200, default="TBD")
    year = models.CharField(max_length=200, default="TBD")
    trim = models.CharField(max_length=200, default="TBD")
    body = models.CharField(max_length=200, default="TBD")

    def __str__(self):
        return f"{self.vin}"

class Inquiry(models.Model):
    inquiry_id = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    create_date = models.DateTimeField(db_default=Now())
    problem = models.CharField(max_length=1000)
    mech_approve_repair = models.BooleanField(default=False)
    customer_approve_repair = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.inquiry_id is None:
            self.inquiry_id = f"{get_timestamp()}{generate_random_id()}"
        return super().save(*args, **kwargs)