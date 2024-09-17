from django.test import TestCase
from .forms import VisitorDetailForm

class TestVisitorDetailForm(TestCase):

    def test_form_is_valid(self):
        """Test that the form is valid with correct data."""
        form_data = {
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'weight': 70,
            'height': 175,
            'full_name': 'John Doe'
        }
        form = VisitorDetailForm(data=form_data)
        self.assertTrue(form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        """Test that the form is invalid with incorrect data."""
        form_data = {
            'email': '',  
            'phone_number': '1234567890',
            'weight': 70,
            'height': 175,
            'full_name': 'John Doe'
        }
        form = VisitorDetailForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="No Email but form is valid")
        