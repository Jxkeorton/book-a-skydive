from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaneList.as_view(), name='experienced'),
    path('<slug:slug>/', views.plane_detail, name='plane_detail'),
    path(
        'edit_booking/<int:booking_id>/',
        views.edit_booking,
        name='edit_booking'
    ),
    path(
        'delete_booking/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking'
    ),
]
