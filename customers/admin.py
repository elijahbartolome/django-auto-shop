from django.contrib import admin

# Register your models here.
from .models import Customer, Vehicle, Inquiry

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date"]

class VehicleAdmin(admin.ModelAdmin):
    list_display = ["vin"]

class InquiryAdmin(admin.ModelAdmin):
    list_display = ["get_customer_name", "get_vehicle_vin"]

    @admin.display(description="Customer Name")
    def get_customer_name(self, obj):
        return obj.customer.name
    
    @admin.display(description="VIN")
    def get_vehicle_vin(self, obj):
        return obj.vehicle.vin

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Inquiry, InquiryAdmin)