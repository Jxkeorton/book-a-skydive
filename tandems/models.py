from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class TandemDay(models.Model):
    date = models.DateField(unique=True)
    max_tandems = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError("Cannot create a TandemDay in the past.")

    @property
    def total_booked(self):
        return sum(slot.booked_tandems for slot in self.timeslots.all())

    @property
    def slots_available(self):
        return self.max_tandems > self.total_booked

class TandemTimeSlot(models.Model):
    day = models.ForeignKey(TandemDay, related_name='timeslots', on_delete=models.CASCADE)
    time = models.TimeField()
    max_tandems = models.PositiveIntegerField(default=6)
    booked_tandems = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('day', 'time')

    def __str__(self):
        return f'{self.day.date} at {self.time}'

    @property
    def slots_available(self):
        return self.max_tandems > self.booked_tandems

class VisitorDetail(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    height = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    full_name = models.CharField(max_length=100)
    timeslot = models.ForeignKey('TandemTimeSlot', related_name='visitor_details', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name} - {self.email}'