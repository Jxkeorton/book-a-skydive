from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import JumpSlot, JumpBooking
from .forms import BookingForm


class PlaneList(LoginRequiredMixin, generic.ListView):
    template_name = "experienced/index.html"
    paginate_by = 6

    def get_queryset(self):
        try:
            return JumpSlot.objects.all()
        except JumpSlot.DoesNotExist:
            messages.error(self.request, "Could not load the jump slots.")
            return []
        except Exception as e:
            messages.error(
                self.request, "An error occurred while loading the slots."
            )
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_bookings = JumpBooking.objects.filter(user=self.request.user)
        booked_slots = user_bookings.values_list(
            'plane_departure__id',
            flat=True
        )

        # Group slots by date
        slots = self.get_queryset()
        grouped_slots = {}
        for slot in slots:
            date = slot.departure.date()
            if date not in grouped_slots:
                grouped_slots[date] = []
            grouped_slots[date].append(slot)

        context['booked_slots'] = booked_slots
        context['slots_by_date'] = grouped_slots
        return context


@login_required
def plane_detail(request, slug):
    """
    View for displaying details of a specific jump slot and managing bookings.

    Shows the details of a jump slot, including users who have booked it.
    Allows the logged-in user to create or update their booking for the slot.
    """
    jump_slot = get_object_or_404(JumpSlot, slug=slug)
    users = jump_slot.users.all()

    existing_booking = JumpBooking.objects.filter(
                            user=request.user, plane_departure=jump_slot
                        ).first()
    user_has_booking = existing_booking is not None

    if request.method == "POST":
        form = BookingForm(request.POST, instance=existing_booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.plane_departure = jump_slot
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
    """
    View for editing an existing booking.

    Allows the user to modify their booking details for a specific jump slot.
    """
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

    return render(
        request,
        'experienced/edit_booking.html',
        {'form': form, 'jump_slot': jump_slot}
    )


@login_required
def delete_booking(request, booking_id):
    """
    View to delete a booking.

    Allows the user to delete their own booking.
    Redirects to the plane detail page
    after deletion.
    """
    booking = get_object_or_404(JumpBooking, id=booking_id)

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
            'plane_detail',
            kwargs={'slug': booking.plane_departure.slug})
        )
