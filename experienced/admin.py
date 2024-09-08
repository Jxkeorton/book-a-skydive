from django.contrib import admin
from .models import Plane, JumpSlot, JumpBooking


class PlaneAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Plane records.

    - Displays the plane's name and capacity in the list view.
    - Allows searching by the plane's name.
    - Orders planes alphabetically by name.
    """
    list_display = ('name', 'capacity')
    search_fields = ('name',)
    ordering = ('name',)


class JumpSlotAdmin(admin.ModelAdmin):
    """
    Admin interface for managing JumpSlot records.

    - Displays the associated plane, departure time,
      and available slots in the list view.
    - Filters by plane and departure time.
    - Allows searching by the plane's name.
    - Orders jump slots by departure time in descending order.
    """
    list_display = ('plane', 'departure', 'available_slots')
    list_filter = ('plane', 'departure')
    search_fields = ('plane__name',)
    ordering = ('-departure',)


class JumpBookingAdmin(admin.ModelAdmin):
    """
    Admin interface for managing JumpBooking records.

    - Displays the user, plane departure, and booking date in the list view.
    - Filters by plane, departure time, and booking date.
    - Allows searching by the user's username and plane's name.
    - Orders bookings by booking date in descending order.
    """
    list_display = ('user', 'plane_departure', 'booking_date')
    list_filter = (
        'plane_departure__plane', 'plane_departure__departure', 'booking_date'
    )
    search_fields = ('user__username', 'plane_departure__plane__name')
    ordering = ('-booking_date',)


admin.site.register(Plane, PlaneAdmin)
admin.site.register(JumpSlot, JumpSlotAdmin)
admin.site.register(JumpBooking, JumpBookingAdmin)
