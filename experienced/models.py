from django.db import models
from django.conf import settings
from django.db.models import F
from django.utils.text import slugify


class Plane(models.Model):
    """
    Model representing an aircraft used for skydiving.

    Attributes:
        name (str): The name of the plane.
        capacity (int): The maximum number of jumpers the plane can accommodate.
    """
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class JumpSlot(models.Model):
    """
    Model representing a scheduled skydiving jump slot.

    Attributes:
        plane (Plane): The plane assigned for the jump.
        departure (DateTimeField): The scheduled time for the jump.
        available_slots (int): The number of available spots for jumpers.
        slug (SlugField): A unique slug generated based on the plane name and a count.
        users (ManyToManyField): Users who have booked this jump slot.
    """
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure = models.DateTimeField()
    available_slots = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="jump_slots", blank=True
    )

    def __str__(self):
        return f"{self.plane.name} on {self.departure}"

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a unique slug if it doesn't exist.
        The slug is based on the plane's name and a count of jump slots for that plane.
        """
        if not self.slug:
            count = JumpSlot.objects.filter(plane=self.plane).count() + 1
            slug_str = f"{self.plane.name}-{count}"
            self.slug = slugify(slug_str)

        super().save(*args, **kwargs)


class JumpBooking(models.Model):
    """
    Model representing a booking for a specific jump slot.

    Attributes:
        user (User): The user who made the booking.
        plane_departure (JumpSlot): The specific jump slot booked.
        booking_date (DateTimeField): The date the booking was made.
        jump_type (str): The type of jump booked, with available choices (Tracking, Solo, AFF, Wingsuit).
    """
    
    JUMP_TYPE_CHOICES = [
        ('TRACKING', 'Tracking Jump'),
        ('SOLO', 'Solo Jump'),
        ('AFF', 'Accelerated Freefall (AFF)'),
        ('WINGSUIT', 'Wingsuit Jump'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    plane_departure = models.ForeignKey(JumpSlot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    jump_type = models.CharField(
        max_length=20, choices=JUMP_TYPE_CHOICES, default='SOLO'
    )

    def __str__(self):
        return (
            f"{self.user.username} booked {self.plane_departure.plane.name} "
            f"on {self.plane_departure.departure}"
        )

    def save(self, *args, **kwargs):
        """
        Override the save method to decrease available slots by one when a booking is created.
        Raises a ValueError if there are no available slots left.
        """
        if not self.pk:  # Only decrease slots on new bookings
            if self.plane_departure.available_slots > 0:
                self.plane_departure.available_slots = F('available_slots') - 1
                self.plane_departure.users.add(self.user)
                self.plane_departure.save(update_fields=['available_slots'])
            else:
                raise ValueError("No available slots left for this jump.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Override the delete method to increase available slots by one when a booking is deleted.
        """
        self.plane_departure.available_slots = F('available_slots') + 1
        self.plane_departure.users.remove(self.user)
        self.plane_departure.save(update_fields=['available_slots'])
        super().delete(*args, **kwargs)
