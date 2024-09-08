from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import F
from .models import TandemDay, TandemTimeSlot
from .forms import DaySelectForm, TimeSlotSelectForm, VisitorDetailForm


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
            return redirect('select_timeslot', date=selected_day)
    return render(request, 'tandems/select_day.html', {'form': form})


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
            return redirect('visitor_details')
    else:
        form = TimeSlotSelectForm(day)

    return render(
        request,
        'tandems/select_timeslot.html',
        {'day': day, 'form': form, 'timeslots': timeslots}
    )


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
        return redirect('select_day')

    timeslot = get_object_or_404(TandemTimeSlot, id=timeslot_id)

    if request.method == 'POST':
        form = VisitorDetailForm(request.POST)
        if form.is_valid():
            visitor_detail = form.save(commit=False)
            visitor_detail.timeslot = timeslot
            visitor_detail.save()
            timeslot.booked_tandems += 1
            timeslot.save()  # Update the timeslot after booking is confirmed
            del request.session['selected_timeslot_id']
            messages.success(
                request,
                f'Booking confirmed for {timeslot.time} on {timeslot.day.date}'
            )
            return redirect('booking_success')
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
