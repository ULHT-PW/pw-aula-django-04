from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Flight, Passenger


# Create your views here.

def index_view(request):
    return render(request, 'flights\index.html', {
        'flights': Flight.objects.all()
    })


def flight_view(request, flight_id):
    f = Flight.objects.get(id=flight_id)

    return render(request, 'flights\eflight.html', {
        'flight': f,
        'passengers': f.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight_id),
    })


def book_view(request, flight_id):
    if request.method == 'POST':
        f = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(id=request.POST['passenger'])
        passenger.flights.add(f)
        return HttpResponseRedirect(reverse('flights:flight', args=(f.id,)))
    

def passenger_book_view(request, passenger_id):
    if request.method == 'POST':
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(id=request.POST['flight'])
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flights:passenger', args=(passenger.id,)))
    

def remove_flight_view(request, flight_id, passenger_id):
    passenger = Passenger.objects.get(id=passenger_id)
    flight = Flight.objects.get(id=flight_id)
    passenger.flights.remove(flight)
    return HttpResponseRedirect(reverse('flights:passenger', args=(passenger.id,)))




def passenger_view(request, passenger_id):
    
    passenger = Passenger.objects.get(id=passenger_id)
    context = {
        'passenger':passenger,
        'non_flights':Flight.objects.exclude(passengers__id=passenger.id),
        }
    return render(request, 'flights/passenger.html', context)