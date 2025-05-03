from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Inquiry, Customer, Vehicle

from .email_ops import send_inquiry_email, notify_admin_about_inquiry

import requests
import json

# Create your views here.
def detail(request, inquiry_id):
    inquiry = get_object_or_404(Inquiry, inquiry_id=inquiry_id)

    return render(request, "customers/detail.html", {"inquiry": inquiry})

def newCustomer(request):
    def get_dictionary_by_key_value(dictionaries, key, value):
        for dictionary in dictionaries:
            if key in dictionary and dictionary[key] == value:
                return dictionary
            
    def get_details(vin):
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json'
        r = requests.get(url)
        data = r.json()['Results']

        details = {
            "Make" : get_dictionary_by_key_value(data, "VariableId", 26)["Value"],
            "Model" : get_dictionary_by_key_value(data, "VariableId", 28)["Value"],
            "Model Year" : get_dictionary_by_key_value(data, "VariableId", 29)["Value"],
            "Trim" : get_dictionary_by_key_value(data, "VariableId", 38)["Value"],
            "Body Class" : get_dictionary_by_key_value(data, "VariableId", 5)["Value"]
        }

        return details

    if request.method == "POST":
        c = Customer(name=request.POST["name"], phone_number=request.POST["phone_number"], email=request.POST["email"])
        c.save()

        details = get_details(request.POST["vehicle_identification_number"])

        v = Vehicle(vin=request.POST["vehicle_identification_number"], make=details["Make"], 
                    model=details["Model"], year=details["Model Year"],
                    trim=details["Trim"], body=details["Body Class"])
        
        v.save()

        i = Inquiry(customer=c, vehicle=v, problem=request.POST["problem"])
        i.save()

        send_inquiry_email(i, c.email, request)
        notify_admin_about_inquiry(i, c.name)
        return render(request, "customers/index.html")
