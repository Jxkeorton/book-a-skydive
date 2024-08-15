from django.http import HttpResponse
from django.shortcuts import render

def tandems_list(request):
    """
    Renders the Tandem page
    """

    return render(
        request,
        template_name = "tandems/tandem.html",
    )