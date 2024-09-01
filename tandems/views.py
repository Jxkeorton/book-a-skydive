from django.shortcuts import render, get_object_or_404, redirect
from .models import TandemDay, TandemTimeSlot
from .forms import DaySelectForm, TimeSlotSelectForm, VisitorDetailForm
from django.contrib import messages
from django.db.models import F

def select_day(request):
    form = DaySelectForm()
    if request.method == 'POST':
        form = DaySelectForm(request.POST)
        if form.is_valid():
            selected_day = form.cleaned_data['date']
            return redirect('select_timeslot', date=selected_day)
    return render(request, 'tandems/select_day.html', {'form': form})

def select_timeslot(request, date):
    day = get_object_or_404(TandemDay, date=date)
    timeslots = day.timeslots.filter(booked_tandems__lt=F('max_tandems'))

    if request.method == 'POST':
        form = TimeSlotSelectForm(day, request.POST)
        if form.is_valid():
            timeslot = form.cleaned_data['timeslot']
            request.session['selected_timeslot_id'] = timeslot.id  # Store the selected timeslot in the session
            return redirect('visitor_details')

    else:
        form = TimeSlotSelectForm(day)

    return render(request, 'tandems/select_timeslot.html', {'day': day, 'form': form, 'timeslots': timeslots})

def visitor_details(request):
    timeslot_id = request.session.get('selected_timeslot_id')
    if not timeslot_id:
        return redirect('select_day')  # If no timeslot in session, redirect to select day

    timeslot = get_object_or_404(TandemTimeSlot, id=timeslot_id)

    if request.method == 'POST':
        form = VisitorDetailForm(request.POST)
        if form.is_valid():
            visitor_detail = form.save(commit=False)
            visitor_detail.timeslot = timeslot
            visitor_detail.save()
            timeslot.booked_tandems += 1
            timeslot.save()  # Update the timeslot after booking is confirmed
            del request.session['selected_timeslot_id']  # Clear the session data
            messages.success(request, f'Booking confirmed for {timeslot.time} on {timeslot.day.date}')
            return redirect('booking_success')
    else:
        form = VisitorDetailForm()

    return render(request, 'tandems/details.html', {'form': form, 'timeslot': timeslot})

def booking_success(request):
    return render(request, 'tandems/booking_success.html')
