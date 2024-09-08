from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import F
from django.contrib import messages
from .models import AFFCourse
from .forms import VisitorDetailForm


class CoursesList(generic.ListView):
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
            visitor_detail.save()
            course.booked_slots += 1
            course.save()
            messages.success(request, f'Booking confirmed for {course.date}')
            return redirect('course_booking_success')
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
