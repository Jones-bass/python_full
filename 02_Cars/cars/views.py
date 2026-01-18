from django.shortcuts import render

# Create your views here.
from cars.models import Car

def car_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)

    return render (
        request,
        'cars.html',
        {'cars': cars }
    )  






   
