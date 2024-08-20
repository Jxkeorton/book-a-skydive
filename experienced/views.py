from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import JumpSlot

class PlaneList(generic.ListView):
    queryset = JumpSlot.objects.all()
    template_name = "experienced/index.html"
    paginate_by = 6
    
def plane_detail(request, slug):
    jump_slot = get_object_or_404(JumpSlot, slug=slug)
    users = jump_slot.users.all()
    
    
    return render(
        request,
        "experienced/plane-detail.html",
        {'users': users, 'jump_slot': jump_slot},
    )