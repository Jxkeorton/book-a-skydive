from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import F
from django.contrib import messages
from .models import AFFCourse
from .forms import VisitorDetailForm


class CoursesList(generic.ListView):
    model = AFFCourse
    template_name = "courses/list_courses.html"
    context_object_name = 'courses'
    paginate_by = 6

    def get_queryset(self):
        return AFFCourse.objects.filter(
            booked_slots__lt=F('max_slots')
        ).order_by('date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for course in context['object_list']:
            course.available_slots = course.max_slots - course.booked_slots
        return context


def visitor_details(request, course_id):
    course = get_object_or_404(AFFCourse, id=course_id)

    if request.method == 'POST':
        form = VisitorDetailForm(request.POST)
        if form.is_valid():
            visitor_detail = form.save(commit=False)
            visitor_detail.course = course
            visitor_detail.save()
            course.booked_slots += 1
            course.save()  # Update the course after booking is confirmed
            messages.success(request, f'Booking confirmed for {course.date}')
            return redirect('booking_success')
    else:
        form = VisitorDetailForm()

    return render(
        request, 'courses/details.html',
        {'form': form, 'date': course.date}
    )


def booking_success(request):
    return render(request, 'courses/booking_success.html')
