# tandems/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import TandemDay, TandemTimeSlot
from django.db.models import F
from .forms import DaySelectForm, TimeSlotSelectForm
from django.contrib import messages

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
            timeslot.booked_tandems += 1
            timeslot.save()
            messages.success(request, f'Booking confirmed for {timeslot.time} on {day.date}')
            return redirect('booking_success')

    else:
        form = TimeSlotSelectForm(day)

    return render(request, 'tandems/select_timeslot.html', {'day': day, 'form': form, 'timeslots': timeslots})

def booking_success(request):
    return render(request, 'tandems/booking_success.html')
