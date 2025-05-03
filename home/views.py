from django.shortcuts import render
from .forms import NewCustomerForm

# Create your views here.
def home(request):
    context = {}
    context['form'] = NewCustomerForm()

    return render(request, "home/index.html", context)