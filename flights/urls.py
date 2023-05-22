from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('',views.index_view, name='index'),
    path('flight/<int:flight_id>', views.flight_view, name='flight'),
    path('flight/<int:flight_id>/book', views.book_view, name='book'),
    path('passenger/<int:passenger_id>', views.passenger_view, name='passenger'),
    path('passenger/<int:passenger_id>/book', views.passenger_book_view, name='passenger_book'),
    path('remove/<int:flight_id>/<int:passenger_id>', views.remove_flight_view, name='remove'),
]
