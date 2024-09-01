from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses, name='list_courses'),  # List available AFF courses
    path('visitor_details/', views.visitor_details, name='visitor_details'),  # Page for entering visitor details
    path('booking_success/', views.booking_success, name='booking_success'),  # Booking success page
]
