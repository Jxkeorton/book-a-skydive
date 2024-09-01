from django.contrib import admin
from .models import AFFCourse, VisitorDetail

@admin.register(AFFCourse)
class AFFCourseAdmin(admin.ModelAdmin):
    list_display = ('date', 'max_slots', 'booked_slots', 'slots_available')
    list_filter = ('date',)
    search_fields = ('date',)
    readonly_fields = ('slots_available',)

@admin.register(VisitorDetail)
class VisitorDetailAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'course')
    list_filter = ('course',)
    search_fields = ('full_name', 'email', 'course__date')
