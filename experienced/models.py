from django.db import models
from django.conf import settings
from django.db.models import F

class Plane(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()  # Maximum number of jumpers

    def __str__(self):
        return self.name

class JumpSlot(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure = models.DateTimeField()
    available_slots = models.IntegerField()

    def __str__(self):
        return f"{self.plane.name} on {self.departure}"

class JumpBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plane_departure = models.ForeignKey(JumpSlot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.plane_departure.plane.name} on {self.plane_departure.departure}"

    # override the save method
    def save(self, *args, **kwargs):
        # Decrease available slots by one when a booking is created
        if not self.pk:  # Only decrease available slots when the booking is created for the first time
            if self.plane_departure.available_slots > 0:
                self.plane_departure.available_slots = F('available_slots') - 1
                self.plane_departure.save(update_fields=['available_slots'])
            else:
                raise ValueError("No available slots left for this jump.")
        super().save(*args, **kwargs)
    
    # Override the delete method
    def delete(self, *args, **kwargs):
        # Increase available slots by one when a booking is deleted
        self.plane_departure.available_slots = F('available_slots') + 1
        self.plane_departure.save(update_fields=['available_slots'])
        super().delete(*args, **kwargs)
