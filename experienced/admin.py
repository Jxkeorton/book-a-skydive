from django.contrib import admin
from .models import Plane, JumpSlot, JumpBooking

class PlaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
    search_fields = ('name',)
    ordering = ('name',)

class JumpSlotAdmin(admin.ModelAdmin):
    list_display = ('plane', 'jump_date', 'available_slots')
    list_filter = ('plane', 'jump_date')
    search_fields = ('plane__name',)
    ordering = ('-jump_date',)

class JumpBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'plane_departure', 'booking_date')
    list_filter = ('plane_departure__plane', 'plane_departure__jump_date', 'booking_date')
    search_fields = ('user__username', 'plane_departure__plane__name')
    ordering = ('-booking_date',)

admin.site.register(Plane, PlaneAdmin)
admin.site.register(JumpSlot, JumpSlotAdmin)
admin.site.register(JumpBooking, JumpBookingAdmin)
