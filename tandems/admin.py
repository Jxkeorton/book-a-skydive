from django.contrib import admin
from .models import TandemDay, TandemTimeSlot, VisitorDetail


@admin.register(TandemDay)
class TandemDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'max_tandems', 'total_booked', 'slots_available')
    list_filter = ('date',)
    search_fields = ('date',)
    readonly_fields = ('total_booked', 'slots_available')


@admin.register(TandemTimeSlot)
class TandemTimeSlotAdmin(admin.ModelAdmin):
    list_display = (
        'day',
        'time',
        'max_tandems',
        'booked_tandems',
        'slots_available'
    )
    list_filter = ('day', 'time',)
    search_fields = ('day__date', 'time')
    readonly_fields = ('slots_available',)


@admin.register(VisitorDetail)
class VisitorDetailAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'weight',
        'height',
        'timeslot'
    )
    list_filter = ('timeslot', 'email',)
    search_fields = ('full_name', 'email', 'phone_number',)
    readonly_fields = ('email', 'phone_number', 'weight', 'height', 'timeslot')
