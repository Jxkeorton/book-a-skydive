from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import AFFCourse, VisitorDetail
from .forms import VisitorDetailForm


class CoursesList(LoginRequiredMixin, generic.ListView):
    """
    Displays a paginated list of AFFCourses with available slots.

    - Filters out courses that are fully booked.
    - Orders courses by date in ascending order.
    - Adds the number of available slots for each course to the context.
    """
    model = AFFCourse
    template_name = "courses/list_courses.html"
    context_object_name = 'courses'
    paginate_by = 6
    login_url = '/'  # Redirect to home if not logged in
    redirect_field_name = None

    def handle_no_permission(self):
        """
        Customizes the behavior when the user doesn't have permission
        (i.e., not logged in). Redirects to home with a message.
        """
        messages.info(
            self.request,
            "Please create a profile to book a course online."
        )
        return redirect(self.login_url)

    def get_queryset(self):
        """
        Returns a queryset of AFFCourses where there are still available slots.
        """
        return AFFCourse.objects.filter(
            booked_slots__lt=F('max_slots')
        ).order_by('date')

    def get_context_data(self, **kwargs):
        """
        Adds the number of available slots to each course in the context.
        """
        context = super().get_context_data(**kwargs)
        for course in context['object_list']:
            course.available_slots = course.max_slots - course.booked_slots
        return context


@login_required(login_url='/')
def visitor_details(request, course_id):
    """
    Handles the form submission for visitor details.

    - Retrieves the AFFCourse by `course_id`.
    - On POST: Validates and saves the visitor's details,
      increments booked slots for the course,
      and redirects to the success page.
    - On GET: Displays an empty form for entering visitor details.

    Args:
        request: The HTTP request object.
        course_id: The ID of the AFFCourse to book.

    Returns:
        A rendered template for booking or redirects to the success page.
    """
    course = get_object_or_404(AFFCourse, id=course_id)

    if request.method == 'POST':
        form = VisitorDetailForm(request.POST)
        if form.is_valid():
            visitor_detail = form.save(commit=False)
            visitor_detail.course = course
            visitor_detail.user = request.user
            visitor_detail.save()
            course.booked_slots += 1
            course.save()
            messages.success(request, f'Booking confirmed for {course.date}')
            return redirect('courses:course_booking_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VisitorDetailForm()

    return render(
        request, 'courses/details.html',
        {'form': form, 'date': course.date}
    )


def booking_success(request):
    """
    Displays the booking success page.

    This view is rendered after a successful booking.
    """
    return render(request, 'courses/booking_success.html')


@login_required
def delete_booking(request, booking_id):
    """
    View to delete a booking.

    Allows the user to delete their own booking.
    Redirects to the plane detail page
    after deletion.
    """
    booking = get_object_or_404(VisitorDetail, id=booking_id)

    if booking.user == request.user:
        try:
            booking.delete()
            messages.success(request, 'Booking deleted successfully!')
        except Exception as e:
            messages.error(
                request,
                'An error occurred while deleting the booking.'
            )
    else:
        messages.error(request, 'You can only delete your own bookings!')

    return redirect(
        reverse(
            'userprofile:user_profile'
        )
    )


@login_required(login_url='/')
def edit_booking(request, booking_id):
    """
    View to edit an existing booking.

    Retrieves the VisitorDetail by `booking_id`, displays
    a form pre-filled with the current details, and updates
    the booking upon valid submission.

    Args:
        request: The HTTP request object.
        booking_id: The ID of the VisitorDetail to edit.

    Returns:
        A rendered template with the form for editing the booking.
    """
    booking = get_object_or_404(VisitorDetail, id=booking_id)

    print("triggered edit course booking")

    if booking.user != request.user:
        messages.error(request, "You can only edit your own bookings!")
        return redirect('userprofile:user_profile')

    if request.method == 'POST':
        form = VisitorDetailForm(data=request.POST, instance=booking)
        print(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your booking has been updated successfully!'
            )
            return redirect('userprofile:user_profile')
        else:
            print(form.errors)
    else:
        form = VisitorDetailForm(instance=booking)

    return render(request, 'index.html', {'form': form, 'booking': booking})
