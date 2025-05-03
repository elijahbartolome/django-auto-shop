from django import forms
from phonenumber_field.formfields import PhoneNumberField

class NewCustomerForm(forms.Form):
    name = forms.CharField(max_length=200)
    vehicle_identification_number = forms.CharField(max_length=40)
    problem = forms.CharField(max_length=1000)
    phone_number = PhoneNumberField(region="CA")
    email = forms.EmailField(max_length=200)