from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class AFFCourse(models.Model):
    date = models.DateField(unique=True)
    max_slots = models.PositiveIntegerField(default=6)
    booked_slots = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'AFF Course on {self.date}'

    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError("Cannot schedule a course in the past.")
        # Check if there's already a course scheduled for the same week
        if AFFCourse.objects.filter(
            date__week=self.date.isocalendar()[1]
        ).exclude(id=self.id).exists():

            raise ValidationError(
                "A course is already scheduled for this week."
            )

    @property
    def slots_available(self):
        return self.max_slots > self.booked_slots


class VisitorDetail(models.Model):
    course = models.ForeignKey(
        AFFCourse, related_name='bookings', on_delete=models.CASCADE
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.full_name} - {self.course.date}'
