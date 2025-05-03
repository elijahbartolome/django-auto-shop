from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path("<str:inquiry_id>/", views.detail, name="detail"),
    path("newCustomer", views.newCustomer, name="newCustomer"),
]