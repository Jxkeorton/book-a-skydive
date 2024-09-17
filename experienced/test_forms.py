from django.test import TestCase
from .forms import BookingForm

class TestBookingForm(TestCase):
    
    def test_form_is_valid(self):
        """ Test for all fields"""
        form = BookingForm({
            'jump_type': 'SOLO'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
        
    def test_form_wrong_jump_type(self):
        """ Test for incorrect jump_type"""
        form = BookingForm({
            'jump_type': 'JAZZ'
        })
        self.assertFalse(form.is_valid(), msg="Wrong jump type entered but Form is valid")