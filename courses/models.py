from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


class AFFCourse(models.Model):
    """
    Model representing an AFF (Accelerated Free Fall) course.

    Attributes:
        date (DateField): The date the course is scheduled for. Must be unique.
        max_slots (PositiveIntegerField):
        The maximum number of participants allowed.
        booked_slots (PositiveIntegerField):
        The number of participants already booked.
    """
    date = models.DateField(unique=True)
    max_slots = models.PositiveIntegerField(default=6)
    booked_slots = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'AFF Course on {self.date}'

    def clean(self):
        """
        Custom validation to ensure:
        1. The course date is not in the past.
        2. No other course is scheduled for the same week.

        Raises:
            ValidationError: If the course date
            is in the past or if another course
            is already scheduled in the same week.
        """
        if self.date < timezone.now().date():
            raise ValidationError("Cannot schedule a course in the past.")

        if AFFCourse.objects.filter(
            date__week=self.date.isocalendar()[1]
        ).exclude(id=self.id).exists():
            raise ValidationError(
                "A course is already scheduled for this week."
            )

    @property
    def slots_available(self):
        """
        Returns True if there are available slots for the course,
        otherwise False.
        """
        return self.max_slots > self.booked_slots


class VisitorDetail(models.Model):
    """
    Model representing details of a visitor booking a course.

    Attributes:
        course (ForeignKey): The AFFCourse the visitor is booking for.
        email (EmailField): The visitor's email address.
        phone_number (CharField): The visitor's contact number (max length 15).
        weight (PositiveIntegerField): The visitor's weight.
        height (PositiveIntegerField): The visitor's height.
        full_name (CharField): The visitor's full name.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='course_bookings', null=True
    )
    course = models.ForeignKey(
        'AFFCourse', related_name='bookings', on_delete=models.CASCADE
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.full_name} - {self.course.date}'

    def delete(self, *args, **kwargs):
        """
        Override the delete method to adjust booked_slots
        before deleting the booking.
        """
        # Decrement the booked_slots of the associated course
        if self.course.booked_slots > 0:
            self.course.booked_slots -= 1
            self.course.save()
        super().delete(*args, **kwargs)
