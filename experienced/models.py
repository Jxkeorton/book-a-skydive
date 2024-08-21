from django.db import models
from django.conf import settings
from django.db.models import F
from django.utils.text import slugify

class Plane(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()  # Maximum number of jumpers

    def __str__(self):
        return self.name

class JumpSlot(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure = models.DateTimeField()
    available_slots = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)  # Slug field to store the URL-friendly string
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="jump_slots", blank=True)

    def __str__(self):
        return f"{self.plane.name} on {self.departure}"
    
    def save(self, *args, **kwargs):
        # Automatically generate a slug based on the plane name and departure count
        if not self.slug:
            # Get the count of existing JumpSlots for this plane
            count = JumpSlot.objects.filter(plane=self.plane).count() + 1
            slug_str = f"{self.plane.name}-{count}"
            self.slug = slugify(slug_str)

        super().save(*args, **kwargs)

class JumpBooking(models.Model):
    # Constants for jump types
    TRACKING = 'TRACKING'
    SOLO = 'SOLO'
    AFF = 'AFF'  # Accelerated Freefall
    WINGSUIT = 'WINGSUIT'

    JUMP_TYPE_CHOICES = [
        (TRACKING, 'Tracking Jump'),
        (SOLO, 'Solo Jump'),
        (AFF, 'Accelerated Freefall (AFF)'),
        (WINGSUIT, 'Wingsuit Jump'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plane_departure = models.ForeignKey(JumpSlot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    jump_type = models.CharField(max_length=20, choices=JUMP_TYPE_CHOICES, default=SOLO)

    def __str__(self):
        return f"{self.user.username} booked {self.plane_departure.plane.name} on {self.plane_departure.departure}"

    # override the save method
    def save(self, *args, **kwargs):
        # Decrease available slots by one when a booking is created
        if not self.pk:  # Only decrease available slots when the booking is created for the first time
            if self.plane_departure.available_slots > 0:
                self.plane_departure.available_slots = F('available_slots') - 1
                self.plane_departure.users.add(self.user) 
                self.plane_departure.save(update_fields=['available_slots'])
            else:
                raise ValueError("No available slots left for this jump.")
        super().save(*args, **kwargs)
    
    # Override the delete method
    def delete(self, *args, **kwargs):
        # Increase available slots by one when a booking is deleted
        self.plane_departure.available_slots = F('available_slots') + 1
        self.plane_departure.users.remove(self.user) 
        self.plane_departure.save(update_fields=['available_slots'])
        super().delete(*args, **kwargs)
