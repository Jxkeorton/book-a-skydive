from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import BookingForm
from .models import JumpBooking, JumpSlot, Plane
from django.utils import timezone

class TestExperiencedViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@example.com"
        )
         # Create a plane
        self.plane = Plane(
            name="Cessna",
            capacity=17
        )

        # Create a JumpSlot
        self.jump_slot = JumpSlot(
            plane=self.plane,
            departure=timezone.now() + timezone.timedelta(days=1),  # Schedule jump for tomorrow
            available_slots=self.plane.capacity
        )

        # Create a JumpBooking
        self.booking = JumpBooking(
            user=self.user,
            plane_departure=self.jump_slot,
            jump_type="SOLO"
        )
        
        self.plane.save()
        self.jump_slot.save()
        self.booking.save()
        
    def test_render_plane_detail_with_booking_form(self):
        """
        Test that the plane detail page renders correctly with the booking form.
        """
        self.client.login(
            username="myUsername", password="myPassword")
        response = self.client.get(reverse('plane_detail', args=[self.jump_slot.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Cessna", response.content)
        self.assertIsInstance(
            response.context['form'], BookingForm)