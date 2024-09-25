from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class TandemDay(models.Model):
    """
    Represents a specific day for tandem jumps.

    Stores information about the date and maximum number of tandems allowed
    for that day. Includes methods to check the total number of booked tandems
    and the availability of slots.
    """
    date = models.DateField(unique=True)
    max_tandems = models.PositiveIntegerField(default=50)

    def __str__(self):
        """
        Returns a string representation of the date in 'YYYY-MM-DD' format.
        """
        return self.date.strftime('%Y-%m-%d')

    def clean(self):
        """
        Validates that the date of the TandemDay is not in the past.
        """
        if self.date < timezone.now().date():
            raise ValidationError("Cannot create a TandemDay in the past.")

    @property
    def total_booked(self):
        """
        Returns the total number of tandems booked for this day by summing up
        the booked tandems across all time slots.
        """
        return sum(slot.booked_tandems for slot in self.timeslots.all())

    @property
    def slots_available(self):
        """
        Checks if there are available slots for tandem jumps on this day.
        """
        return self.max_tandems > self.total_booked


class TandemTimeSlot(models.Model):
    """
    Represents a specific time slot for tandem jumps on a given day.

    Stores information about the time, maximum number of tandems allowed,
    and the number of booked tandems for this time slot. Includes a method
    to check the availability of slots.
    """
    day = models.ForeignKey(
        TandemDay,
        related_name='timeslots',
        on_delete=models.CASCADE
    )
    time = models.TimeField()
    max_tandems = models.PositiveIntegerField(default=6)
    booked_tandems = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('day', 'time')

    def __str__(self):
        """
        Returns a string representation of the time slot
        in 'YYYY-MM-DD at HH:MM' format.
        """
        return f'{self.day.date} at {self.time}'

    @property
    def slots_available(self):
        """
        Checks if there are available slots for tandem jumps at this time slot.
        """
        return self.max_tandems > self.booked_tandems


class VisitorDetail(models.Model):
    """
    Represents details of a visitor booking a tandem jump.

    Stores information about the visitor's contact details,
    physical attributes,
    and the time slot they have booked. Includes a method to return a string
    representation of the visitor's details.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tandem_bookings'
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    height = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    full_name = models.CharField(max_length=100)
    timeslot = models.ForeignKey(
        'TandemTimeSlot',
        related_name='tandem_timeslot',
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Returns a string representation of the visitor's full name and email.
        """
        return f'{self.full_name} - {self.email}'
