from django import forms
from .models import JumpBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = JumpBooking
        fields = ['jump_type']  # User will choose a plane departure slot

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Capture the user when initializing the form
        super().__init__(*args, **kwargs)
