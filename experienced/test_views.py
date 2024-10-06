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
            departure=timezone.now() + timezone.timedelta(days=1),
            available_slots=self.plane.capacity
        )

        self.plane.save()
        self.jump_slot.save()

    def test_render_plane_detail_with_booking_form(self):
        """
        Test that the plane detail page
        renders correctly with the booking form.
        """
        self.client.login(
            username="myUsername", password="myPassword"
        )
        response = self.client.get(
            reverse('experienced:plane_detail', args=[self.jump_slot.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Cessna", response.content)
        self.assertIsInstance(
            response.context['form'], BookingForm)

    def test_successful_booking_submission(self):
        """Test for booking a specific plane departure"""
        self.client.login(
            username="myUsername", password="myPassword")
        booking_data = {
            'jump_type': 'SOLO'
        }

        # Pass follow=True to follow the redirect after POST request
        response = self.client.post(reverse(
            'experienced:plane_detail',
            args=[self.jump_slot.slug]),
            booking_data,
            follow=True
        )

        # After following the redirect, the status code should be 200
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'myUsername',
            response.content
        )

    def test_edit_booking(self):
        """
        Test editing an existing booking.
        """
        self.client.login(username="myUsername", password="myPassword")

        booking = JumpBooking(
            user=self.user,
            plane_departure=self.jump_slot,
            jump_type="SOLO"
        )
        booking.save()

        self.assertEqual(JumpBooking.objects.filter(user=self.user).count(), 1)
        updated_booking_data = {
            'jump_type': 'WINGSUIT'
        }

        response = self.client.post(
            reverse('experienced:edit_booking', args=[booking.id]),
            updated_booking_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        booking.refresh_from_db()
        self.assertEqual(booking.jump_type, 'WINGSUIT')

        self.assertIn(b'Booking updated successfully.', response.content)

    def test_delete_booking(self):
        """Test that a user can delete their own booking."""
        self.client.login(username="myUsername", password="myPassword")

        booking = JumpBooking(
            user=self.user,
            plane_departure=self.jump_slot,
            jump_type="SOLO"
        )
        booking.save()

        response = self.client.post(
                        reverse(
                            'experienced:delete_booking',
                            args=[booking.id]),
                            follow=True
                        )

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(booking, JumpBooking.objects.all())
        self.assertIn(b'Booking deleted successfully!', response.content)
