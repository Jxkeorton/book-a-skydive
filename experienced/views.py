from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import JumpSlot, JumpBooking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class PlaneList(generic.ListView):
    queryset = JumpSlot.objects.all()
    template_name = "experienced/index.html"
    paginate_by = 6
    
@login_required
def plane_detail(request, slug):
    jump_slot = get_object_or_404(JumpSlot, slug=slug)
    users = jump_slot.users.all()
    
     # Check if the current user has a booking for this plane
    existing_booking = JumpBooking.objects.filter(user=request.user, plane_departure=jump_slot).first()
    user_has_booking = existing_booking is not None
    
    if request.method == "POST":
        # Use the existing booking instance if available, or create a new one
        form = BookingForm(request.POST, instance=existing_booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the current logged-in user
            booking.plane_departure = jump_slot  # Automatically set the plane departure
            booking.save()

            if user_has_booking:
                messages.success(request, 'Booking updated successfully.')
            else:
                messages.success(request, 'Booking completed successfully.')

            return redirect('plane_detail', slug=slug)
    else:
        form = BookingForm(instance=existing_booking)

    return render(
        request,
        "experienced/plane-detail.html",
        {
            'users': users,
            'jump_slot': jump_slot,
            'form': form,
            'user_has_booking': user_has_booking,
            'existing_booking': existing_booking
        },
    )
    
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(JumpBooking, id=booking_id, user=request.user)
    jump_slot = booking.plane_departure

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('plane_detail', slug=jump_slot.slug)
    else:
        form = BookingForm(instance=booking)

    return render(request, 'experienced/edit_booking.html', {'form': form, 'jump_slot': jump_slot})