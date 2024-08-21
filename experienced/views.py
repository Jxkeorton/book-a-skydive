from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import JumpSlot, JumpBooking
from .forms import BookingForm
from django.contrib import messages

class PlaneList(generic.ListView):
    queryset = JumpSlot.objects.all()
    template_name = "experienced/index.html"
    paginate_by = 6
    
def plane_detail(request, slug):
    jump_slot = get_object_or_404(JumpSlot, slug=slug)
    users = jump_slot.users.all()
    
    user_has_booking = False
    if request.user.is_authenticated:
        user_has_booking = JumpBooking.objects.filter(user=request.user, plane_departure=jump_slot).exists()
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the current logged-in user
            booking.plane_departure = jump_slot  # Automatically set the plane departure
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking Completed successfully'
            )
            return redirect('plane_detail', slug=slug)
    
    form = BookingForm()
    
    
    return render(
        request,
        "experienced/plane-detail.html",
        {
            'users': users,
            'jump_slot': jump_slot,
            'form': form,
            'user_has_booking': user_has_booking
        },
    )