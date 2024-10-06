from django.shortcuts import render
from tandems.models import VisitorDetail as TandemVisitorDetail
from courses.models import VisitorDetail as CourseVisitorDetail
from experienced.models import JumpBooking
from django.contrib.auth.decorators import login_required


@login_required
def user_profile_view(request):
    """
    View function for displaying user profile with booked tandem jumps
    and AFF courses.
    """
    user = request.user  # Get the current logged-in user

    # Filter VisitorDetail instances for tandem bookings
    tandem_bookings = TandemVisitorDetail.objects.filter(user=user)

    # Filter CourseVisitorDetail instances for AFF course bookings
    course_bookings = CourseVisitorDetail.objects.filter(user=user)

    # Filter JumpBooking instances for experienced bookings
    experienced_bookings = JumpBooking.objects.filter(user=user)

    has_bookings = (
        tandem_bookings.exists()
        or course_bookings.exists()
        or experienced_bookings.exists()
    )

    # Render the template with the user's bookings
    context = {
        'tandem_bookings': tandem_bookings,
        'course_bookings': course_bookings,
        'experienced_bookings': experienced_bookings,
        'has_bookings': has_bookings,
        'user': user
    }

    return render(request, 'userprofile.html', context)
