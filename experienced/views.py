from django.views import generic
from .models import JumpSlot

class PlaneList(generic.ListView):
    queryset = JumpSlot.objects.all()
    template_name = "experienced/index.html"
    paginate_by = 6