from django import forms
from django.db.models import F
from .models import TandemDay, TandemTimeSlot, VisitorDetail
import re


class DaySelectForm(forms.Form):
    """
    Form for selecting a day for a tandem jump.
    Filters TandemDay objects to only include those with available time slots
    (i.e., where the number of booked tandems is less than the maximum).
    """
    date = forms.ModelChoiceField(
        queryset=TandemDay.objects.filter(
            timeslots__booked_tandems__lt=6
        ).distinct()
    )

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and sets a custom label for the date field.
        """
        super().__init__(*args, **kwargs)
        self.fields['date'].label = "Select a day for your tandem jump"


class TimeSlotSelectForm(forms.Form):
    """
    Form for selecting a time slot on a specific day.

    Filters TandemTimeSlot objects to only include those on the specified day
    where the number of booked tandems is less than the maximum allowed.
    """
    timeslot = forms.ModelChoiceField(queryset=TandemTimeSlot.objects.none())

    def __init__(self, day, *args, **kwargs):
        """
        Initializes the form with a specific day's
        time slots and sets a custom label
        for the timeslot field.

        :param day: The TandemDay instance for which time
        slots are to be filtered.
        """
        super().__init__(*args, **kwargs)
        self.fields['timeslot'].queryset = TandemTimeSlot.objects.filter(
            day=day,
            booked_tandems__lt=F('max_tandems')
        )

        self.fields['timeslot'].label = "Select a time slot"


class VisitorDetailForm(forms.ModelForm):
    """
    Form for capturing visitor details for a tandem jump booking.

    Uses Django's ModelForm to automatically generate form fields based on the
    VisitorDetail model. Customizes widget attributes for better styling.
    """
    class Meta:
        model = VisitorDetail
        fields = ['email', 'phone_number', 'weight', 'height', 'full_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d+$', phone_number):  # Only allows digits
            raise forms.ValidationError("Phone number must be numeric.")
        return phone_number