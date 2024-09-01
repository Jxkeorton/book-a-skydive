from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list_courses'),  # List of available courses
    path('book/<int:course_id>/', views.BookCourseView.as_view(), name='book_course'),  # Book a course
    path('booking_success/', views.booking_success, name='booking_success'),  # Booking success page
]
