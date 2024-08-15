from django.views import generic
from .models import JumpBooking

class PlaneList(generic.ListView):
    queryset = JumpBooking.objects.all()
    template_name = "experienced/index.html"
    paginate_by = 6