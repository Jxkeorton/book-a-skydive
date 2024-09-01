from django.urls import path
from . import views

urlpatterns = [
    path('select-day/', views.select_day, name='select_day'),
    path('select-timeslot/<date>/', views.select_timeslot, name='select_timeslot'),
    path('details/', views.visitor_details, name='visitor_details'),
    path('booking-success/', views.booking_success, name='booking_success'),
]
