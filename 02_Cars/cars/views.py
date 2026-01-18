from django.shortcuts import render

# Create your views here.
from cars.models import Car

def car_view(request):
    cars = Car.objects.all()

    return render (
        request,
        'cars.html',
        {'cars': cars }
    )  






   
