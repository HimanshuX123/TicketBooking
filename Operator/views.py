from django.shortcuts import render
from Customer.models import Passenger


def view(request):
    passengers = Passenger.objects.all()
    return render(request, 'dashboard.html', {'passengers': passengers})
