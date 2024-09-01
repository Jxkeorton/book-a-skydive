from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import AFFCourse
from .forms import CourseSelectForm, VisitorDetailForm
from django.contrib import messages

def list_courses(request):
    courses = AFFCourse.objects.filter(booked_slots__lt=F('max_slots')).order_by('date')
    form = CourseSelectForm(courses=courses)

    if request.method == 'POST':
        form = CourseSelectForm(courses=courses, data=request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            request.session['selected_course_id'] = course.id
            return redirect('visitor_details')

    return render(request, 'tandems/list_courses.html', {'form': form, 'courses': courses})

def visitor_details(request):
    course_id = request.session.get('selected_course_id')
    if not course_id:
        return redirect('list_courses')

    course = get_object_or_404(AFFCourse, id=course_id)

    if request.method == 'POST':
        form = VisitorDetailForm(request.POST)
        if form.is_valid():
            visitor_detail = form.save(commit=False)
            visitor_detail.course = course
            visitor_detail.save()
            course.booked_slots += 1
            course.save()  # Update the course after booking is confirmed
            del request.session['selected_course_id']  # Clear the session data
            messages.success(request, f'Booking confirmed for {course.date}')
            return redirect('booking_success')
    else:
        form = VisitorDetailForm()

    return render(request, 'tandems/details.html', {'form': form, 'course': course})

def booking_success(request):
    return render(request, 'tandems/booking_success.html')
