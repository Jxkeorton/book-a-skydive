from django.db import models
from django.conf import settings

class Plane(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()  # Maximum number of jumpers

    def __str__(self):
        return self.name

class JumpSlot(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    jump_date = models.DateField()
    available_slots = models.IntegerField()

    def __str__(self):
        return f"{self.plane.name} on {self.jump_date}"

class JumpBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    jump_slot = models.ForeignKey(JumpSlot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.jump_slot.plane.name} on {self.jump_slot.jump_date}"
