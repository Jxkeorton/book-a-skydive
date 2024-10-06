from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import AFFCourse, VisitorDetail
from .forms import VisitorDetailForm


class TestVisitorDetailsView(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@example.com"
        )

        self.course = AFFCourse(
            date=timezone.now().date() + timezone.timedelta(days=10),
            max_slots=10,
            booked_slots=5
        )
        self.course.save()

    def test_view_visitor_details_form(self):
        """Test that the visitor details form is rendered correctly."""
        self.client.login(
            username="myUsername", password="myPassword"
        )
        response = self.client.get(
            reverse('courses:course_visitor_details', args=[self.course.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['form'], VisitorDetailForm)

    def test_successful_booking_submission(self):
        """Test booking a course with valid visitor details."""
        self.client.login(
            username="myUsername", password="myPassword"
        )
        booking_data = {
            'email': 'visitor@example.com',
            'phone_number': '1234567890',
            'weight': 70,
            'height': 175,
            'full_name': 'John Doe'
        }

        response = self.client.post(
            reverse('courses:course_visitor_details',
                    args=[self.course.id]),
            booking_data, follow=True
                )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Booking confirmed for', response.content)
        self.assertEqual(
            AFFCourse.objects.get(id=self.course.id).booked_slots, 6
        )
        self.assertTrue(
            VisitorDetail.objects.filter(email='visitor@example.com').exists()
        )
