from django.urls import path
from . import views

app_name = 'tandems' 

urlpatterns = [
    path('select-day/', views.select_day, name='select_day'),
    path('select-timeslot/<date>/', views.select_timeslot, name='select_timeslot'),
    path('details/', views.visitor_details, name='visitor_details'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path(
        'delete_booking/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking'
    ),
]
