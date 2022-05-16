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
        passenger = int(request.POST['passenger'])
        passenger.flights.add(f)
        return HttpResponseRedirect(reverse('flights:flight', args=(f.id)))