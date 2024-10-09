from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from .models import TandemDay, TandemTimeSlot, VisitorDetail
from .forms import DaySelectForm, TimeSlotSelectForm, VisitorDetailForm


def custom_login_required(view_func):
    """
    Custom login_required decorator that adds a message before redirecting.
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(
                request, "Please create a profile to book a Tandem online."
            )
            return redirect('/')
        return view_func(request, *args, **kwargs)
    return wrapper


@custom_login_required
def select_day(request):
    """
    View to select a day for tandem jumps.

    Displays a form for selecting a day. On form submission, redirects
    to the timeslot selection view for the selected day.
    """
    form = DaySelectForm()
    if request.method == 'POST':
        form = DaySelectForm(request.POST)
        if form.is_valid():
            selected_day = form.cleaned_data['date']
            return redirect('tandems:select_timeslot', date=selected_day)
    return render(request, 'tandems/select_day.html', {'form': form})


@login_required(login_url='/')
def select_timeslot(request, date):
    """
    View to select a time slot for a specific day.

    Retrieves available time slots for the selected day and displays
    a form to choose a time slot. On form submission, stores the selected
    time slot in the session and redirects to the visitor details view.
    """
    day = get_object_or_404(TandemDay, date=date)
    timeslots = day.timeslots.filter(booked_tandems__lt=F('max_tandems'))

    if request.method == 'POST':
        form = TimeSlotSelectForm(day, request.POST)
        if form.is_valid():
            timeslot = form.cleaned_data['timeslot']
            request.session['selected_timeslot_id'] = timeslot.id
            return redirect('tandems:visitor_details')
    else:
        form = TimeSlotSelectForm(day)

    return render(
        request,
        'tandems/select_timeslot.html',
        {'day': day, 'form': form, 'timeslots': timeslots}
    )


@login_required(login_url='/')
def visitor_details(request):
    """
    View to enter visitor details for the selected time slot.

    Retrieves the selected time slot from the session and displays a
    form for entering visitor details. On form submission, creates a
    new VisitorDetail entry, updates the time slot's booked tandems,
    and redirects to the booking success view.
    """
    timeslot_id = request.session.get('selected_timeslot_id')
    if not timeslot_id:
        return redirect('tandems:select_day')

    timeslot = get_object_or_404(TandemTimeSlot, id=timeslot_id)

    if request.method == 'POST':
        form = VisitorDetailForm(request.POST)
        if form.is_valid():
            visitor_detail = form.save(commit=False)
            visitor_detail.timeslot = timeslot
            visitor_detail.user = request.user
            visitor_detail.save()
            timeslot.booked_tandems += 1
            timeslot.save()
            del request.session['selected_timeslot_id']
            messages.success(
                request,
                f'Booking confirmed for {timeslot.time} on {timeslot.day.date}'
            )
            return redirect('tandems:booking_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VisitorDetailForm()

    return render(
        request,
        'tandems/details.html',
        {'form': form, 'timeslot': timeslot}
    )


def booking_success(request):
    """
    View to display a successful booking confirmation message.

    Renders a template that informs the user of successful booking.
    """
    return render(request, 'tandems/booking_success.html')


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

    return redirect(reverse('userprofile:user_profile'))


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

    if booking.user != request.user:
        messages.error(request, "You can only edit your own bookings!")
        return redirect('userprofile:user_profile')

    if request.method == 'POST':
        form = VisitorDetailForm(data=request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your booking has been updated successfully!'
            )
            return redirect('userprofile:user_profile')
        else:
            messages.error('There was an error updating your booking, Please try again or contact us.')
    else:
        form = VisitorDetailForm(instance=booking)

    return render(request, 'index.html', {'form': form, 'booking': booking})
