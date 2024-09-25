from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CoursesList.as_view(), name='list_courses'),
    path('visitor_details/<int:course_id>/', views.visitor_details, name='course_visitor_details'),
    path('booking_success/', views.booking_success, name='course_booking_success'),
    path(
        'delete_booking/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking'
    ),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]