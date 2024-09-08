from django import forms
from .models import JumpBooking


class BookingForm(forms.ModelForm):
    """
    Form for creating or updating a JumpBooking.

    The form includes the 'jump_type' field,
    allowing the user to choose a jump type.
    The user is captured during initialization and
    can be used for validation or other logic.
    """
    class Meta:
        model = JumpBooking
        fields = ['jump_type']

    def __init__(self, *args, **kwargs):
        """
        Initializes the BookingForm.

        Captures the user from kwargs and can be used
        to customize behavior based on the user.
        """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
