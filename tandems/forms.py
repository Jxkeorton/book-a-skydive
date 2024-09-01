from django import forms
from django.db.models import F
from .models import TandemDay, TandemTimeSlot

class DaySelectForm(forms.Form):
    date = forms.ModelChoiceField(queryset=TandemDay.objects.filter(timeslots__booked_tandems__lt=6).distinct())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].label = "Select a day for your tandem jump"

class TimeSlotSelectForm(forms.Form):
    timeslot = forms.ModelChoiceField(queryset=TandemTimeSlot.objects.none())

    def __init__(self, day, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['timeslot'].queryset = TandemTimeSlot.objects.filter(day=day, booked_tandems__lt=F('max_tandems'))
        self.fields['timeslot'].label = "Select a time slot"
